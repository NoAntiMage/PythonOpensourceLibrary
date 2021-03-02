# coding: utf-8

from flask import Flask
from flask import request
from flask import jsonify
from jira import JIRA
from jira import JIRAError
import json
import logging
from functools import wraps
import configparser

# options = {'server': server}
# basic_auth = (username, password)


def initialize_log():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%s')

    hterm = logging.StreamHandler()
    hterm.setLevel(logging.INFO)
    hterm.setFormatter(formatter)

    hfile = logging.FileHandler('./log/access.log')
    hfile.setFormatter(formatter)
    logger.addHandler(hterm)
    logger.addHandler(hfile)
    return logger


logger = initialize_log()


def jira_login(func):
    @wraps(func)
    def decorated():
        try:
            data = request.get_data()
            data = json.loads(data)
            basic_auth = (data['login']['username'], data['login']['password'])
            # print(basic_auth)

            config = configparser.ConfigParser()
            config.read('./config/config.conf', encoding='utf-8')
            items = dict(config.items('dev'))
            options = {'server': items['server']}
            # basic_auth = (items['username'], items['password'])
            # print(basic_auth)
            # print(options)
            jira = JIRA(options=options, basic_auth=basic_auth,max_retries=0)
            logger.info('user {} login'.format(data['login']['username']))
            return func(jira)
        except Exception as e:
            logger.error('login failure')
            logger.error(e)
            result = jsonify({'message': 'login failure'})
            result.status_code = 400
            return result
    return decorated


def sell_service(issue_dict):
    fields = set()
    fields = {'project', 'summary', 'description', 'upperComputer', 'lowerComputer', 'productId', 'guestName', 'guestLevel', 'archiveProduct', 'hardwareConfigModelDescription', 'guestArea', 'controlBoxSerialNumber', 'versionName'}
    keys = set(issue_dict.keys())
    print(keys)
    lack_list = list(fields - keys)
    if len(lack_list):
        raise Exception({'参数缺失': lack_list})
    result = dict()
    result.setdefault('project', {'key': issue_dict.get('project')})
    result.setdefault('summary', issue_dict.get('summary'))
    result.setdefault('description', issue_dict.get('description'))
    result.setdefault('issuetype', {'name': '故障 - 售前售后'})
    result.setdefault('customfield_10702', issue_dict.get("upperComputer"))
    result.setdefault('customfield_10703', issue_dict.get("lowerComputer"))
    result.setdefault('customfield_10708', issue_dict.get("productId"))
    result.setdefault('customfield_10602', issue_dict.get("guestName"))
    result.setdefault('customfield_10706', {"value": issue_dict.get("guestLevel")})
    result.setdefault('customfield_10707', {"value": issue_dict.get("archiveProduct")})
    result.setdefault('customfield_10701', issue_dict.get("hardwareConfigModelDescription"))
    result.setdefault('customfield_10720', {"value": issue_dict.get("guestArea")})
    # result.setdefault('customfield_11102', {"value": issue_dict.get("seedGuest")})
    result.setdefault('customfield_11001', issue_dict.get("controlBoxSerialNumber"))
    result.setdefault('customfield_10906', {"value": issue_dict.get("versionName")})
    return result


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello gaussian!\nI am running.'


@app.route('/login', methods=['POST'])
@jira_login
def login(jira):
    current_user = jira.current_user()
    # print('i am %s' % current_user)
    return 'Greeting, %s.' % current_user


@app.route('/version', methods=['POST'])
@jira_login
def version(jira):
    result = "hello world."
    try:
        server_info = jira.server_info()
        assert server_info["serverTitle"] == 'Jira'
        result = jsonify(server_info)
        # print(result)
        # print(type(result))
    except Exception as e:
        logger.error(e)
    finally:
        logger.info(result)
        return result


@app.route('/all_projects', methods=['POST'])
@jira_login
def all_projects(jira):
    result = {'message': 'check your massage'}
    try:
        projects = jira.projects()
        logger.info(projects)
        projects_list = list()
        projects_dict = dict()

        for project in projects:
            tmp = dict()
            tmp.update({'key': project.key})
            tmp.update({'name': project.name})
            tmp.update({'id': project.id})
            projects_list.append(tmp)
        projects_dict = {'all_projects': projects_list}
        print(projects_dict)
        result = projects_dict
    except Exception as e:
        logger.error(e)
    finally:
        logger.info(result)
        result = jsonify(result)
        return result


@app.route('/search_issue', methods=['POST'])
@jira_login
def search_issue(jira):
    result = {'message': 'check your massage'}
    try:
        data = request.get_data()
        data = json.loads(data)
        print(data)
        jql = data['data']['jql']
        print(jql)
        issues = jira.search_issues(jql)
        print(type(issues))
        logger.info(issues)
        issue_list = list()
        for issue in issues:
            issue_list.append({'key': issue.key, 'id': issue.id})
        result = {'issues': issue_list}
    except Exception as e:
        logger.error(e)
    finally:
        logger.info(result)
        result = jsonify(result)
        return result


@app.route('/create_issue', methods=['POST'])
@jira_login
def create_issue(jira):
    result = {'message': 'check your massage'}
    try:
        data = request.get_data()
        data = json.loads(data)
        issue_dict = data['data']
        # print(issue_dict)
        logger.info(issue_dict)
        if issue_dict['project'] == 'SELLSERVIC':
            issue_dict = sell_service(issue_dict)
            print(issue_dict)
        new_issue = jira.create_issue(fields=issue_dict)
        if new_issue:
            result['message'] = 'success'
            result.update({'key': new_issue.key})
            logger.info(new_issue.key)
        else:
            pass
        result = jsonify(result)
    except JIRAError as e:
        print(e)
        if e.response.text:
            text = json.loads(e.response.text)
            text = text["errors"]
            print(text)
            print(type(text))
        else:
            text = e.text
        logger.info(text)
        result['message'] = text
        result = jsonify(result)
        result.status_code = 400
    except Exception as e:
        logger.error(e)
        # result['message'] = str(e)
        result['message'] = e.args[0]
        result = jsonify(result)
        result.status_code = 400
    finally:
        logger.info(result)
        return result


if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0')
    app.run(host='0.0.0.0', port=5000)