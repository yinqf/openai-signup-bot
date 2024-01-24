from config import cf_solver_proxy, proxy


# 获取代理，你可以修改这个方法来对接你的代理服务。返回值的格式为 `http://user:password@123.45.67.89:8080`
def get_proxy():
    return proxy


# 获取代理, 你可以修改这个方法来对接你的代理服务。格式参考 https://yescaptcha.atlassian.net/wiki/spaces/YESCAPTCHA/pages/86409217/CloudFlareTask+CloudFlare5
def get_cf_solver_proxy():
    return cf_solver_proxy
