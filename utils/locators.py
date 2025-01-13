from appium.webdriver.common.appiumby import AppiumBy
class CalculatorLocators:
    BASED_BTTN_XPATH = "//android.widget.Button[@content-desc='{button}']"
    RESULT_ID = "com.sec.android.app.popupcalculator:id/calc_edt_formula"
    @classmethod
    def get_num_locator(cls, num):
        return (AppiumBy.XPATH, cls.BASED_BTTN_XPATH.format(button=num))

    @classmethod
    def get_op_locator(cls, op):
        return (AppiumBy.XPATH, cls.BASED_BTTN_XPATH.format(button=op))
    
    @classmethod
    def get_result(cls):
        return (AppiumBy.ID, cls.RESULT_ID)