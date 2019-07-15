# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云(BlueKing) available.
Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
"""

from common.mymako import render_mako_context


def home(request):
    """
    首页
    """

    from blueking.component.client import ComponentClient
    from conf import default
    # APP应用ID
    bk_app_code = default.APP_ID
    # APP安全密钥
    bk_app_secret = default.APP_TOKEN
    # 用户登录态信息
    bk_token = request.COOKIES.get('bk_token', '')
    print(bk_token)
    common_args = {'bk_token': bk_token,'bk_supplier_account':'admin','user_name':'admin'} # 参数
    # APP应用ID和APP安全密钥如未提供，默认从django settings中获取
    client = ComponentClient(
        bk_app_code=bk_app_code,
        bk_app_secret=bk_app_secret,
        common_args=common_args
    )
    # 参数
    # kwargs = {'bk_biz_id': 1}
    # result = client.cc.get_user_privilege(kwargs)
    result = client.cc.get_user_privilege()
    print(result)
    print(11)

    return render_mako_context(request, '/home_application/index.html')


def dev_guide(request):
    """
    开发指引
    """
    return render_mako_context(request, '/home_application/dev_guide.html')


def contactus(request):
    """
    联系我们
    """
    return render_mako_context(request, '/home_application/contact.html')
