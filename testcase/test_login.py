# import pytest
# class Test_login:
#     # 定义特殊fixture
#     @pytest.fixture()
#     def my_fixture(self):
#         print("我的初始化")
#         yield  # 退出当前函数
#         print("用户数据恢复")
#         def test_first1(self):
#             print("登录：我的第一个pytest")
#         #assert 1 == 2
#     @pytest.mark.debug
#     @pytest.mark.usefixtures("my_fixture") #调用my_fixture
#     def test_first2(self):
#         print("登录：我的第二个pytest")
#         #assert 1 == 1
#
#     @pytest.mark.debug
#     @pytest.mark.usefixtures("my_fixture")
#     def test_first3(self):
#         print("登录：我的第三个pytest")
#         #assert '1' in 'abc'
