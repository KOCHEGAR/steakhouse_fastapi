# For easy building openapi arguments for endpoints
class DocInfo:
    def __init__(self, descr='', summ='', res_descr='', status_code=200, resp_model=None):
        self.description = descr
        self.summary = summ
        self.response_description = res_descr
        self.status_code = status_code
        self.response_model = resp_model
