from datetime import datetime
from flask import render_template, request
from run import app
from wxcloudrun.dao import delete_counterbyid, query_counterbyid, insert_counter, update_counterbyid, gpt_35_api_stream, insert_answer, query_answerbyid
from wxcloudrun.model import Counters, Answer
from wxcloudrun.response import make_succ_empty_response, make_succ_response, make_err_response
import logging
import threading
import sys

# 初始化日志
logger = logging.getLogger('log')
@app.route('/')
def index():
    """
    :return: 返回index页面
    """
    return render_template('index.html')


@app.route('/api/count', methods=['POST'])
def count():
    """
    :return:计数结果/清除结果
    """

    # 获取请求体参数
    params = request.get_json()

    # 检查action参数
    if 'action' not in params:
        return make_err_response('缺少action参数')

    # 按照不同的action的值，进行不同的操作
    action = params['action']

    # 执行自增操作
    if action == 'inc':
        counter = query_counterbyid(1)
        if counter is None:
            counter = Counters()
            counter.id = 1
            counter.count = 1
            counter.created_at = datetime.now()
            counter.updated_at = datetime.now()
            insert_counter(counter)
        else:
            counter.id = 1
            counter.count += 1
            counter.updated_at = datetime.now()
            update_counterbyid(counter)
        return make_succ_response(counter.count)

    # 执行清0操作
    elif action == 'clear':
        delete_counterbyid(1)
        return make_succ_empty_response()

    # action参数错误
    else:
        return make_err_response('action参数错误')


@app.route('/api/count', methods=['GET'])
def get_count():
    """
    :return: 计数的值
    """
    counter = Counters.query.filter(Counters.id == 1).first()
    return make_succ_response(0) if counter is None else make_succ_response(counter.count)

@app.route('/chat/start_task', methods=['POST'])
def chat():
    """
    :return:计数结果/清除结果
    """


    params = request.get_json()
    # 检查参数
    if 'question' not in params:
        return make_err_response('缺少question参数')
    
    print("=========================", file=sys.stderr)

    ans = Answer()
    ans.created_at = datetime.now()
    ans.status = 1
    ans.answer = "请稍等，兔兔正在努力思考中..."
    id = insert_answer(ans)
    question = params['question']
    msg = [{'role': 'user','content':question}]
    thread1 = threading.Thread(target=gpt_35_api_stream, args=(msg, id))
    thread1.start()
    # gpt_35_api_stream(msg, id)
    return make_succ_response(id)


@app.route('/chat/get_id_status', methods=['GET'])
def chat_get_id_status():
    """
    :return:计数结果/清除结果
    """

    # 获取请求体参数
    id = request.args.get('id')
    answer = query_answerbyid(int(id))
    status = answer.status
    return make_succ_response(id)
    

@app.route('/chat/get_id_response', methods=['get'])
def chat_get_id_response():
    """
    :return:计数结果/清除结果
    """

    # 获取请求体参数
    id = request.args.get('id')
    answer_model = query_answerbyid(int(id))
    ans = answer_model.answer
    return make_succ_response(ans)