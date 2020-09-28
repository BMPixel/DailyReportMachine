import random
from selenium import webdriver
import time

driver = webdriver.Chrome()

def quit():
    driver.quit()


def process(account, passwd):
    driver.get("https://xg.hit.edu.cn/zhxy-xgzs/xg_mobile/shsj/loginChange")
    print("# Initialize successfully")
    driver.find_element_by_css_selector("button").click()
    if len(driver.find_elements_by_css_selector(".footer_img4")) > 0:
        # 退出
        driver.find_element_by_css_selector(".footer_img4").click()
        time.sleep(3)
        driver.find_element_by_css_selector("button").click()
        time.sleep(3)
        print("# Quit last account")

    driver.find_element_by_css_selector("input#username").send_keys(account)
    driver.find_element_by_css_selector("input#password").send_keys(passwd)
    driver.find_element_by_css_selector("button.auth_login_btn").click()
    driver.get("https://xg.hit.edu.cn/zhxy-xgzs/xg_mobile/xs/yqxx")
    driver.execute_script("add();")
    time.sleep(2)
    try:
        alert = driver.switch_to.alert
        alert.accept()
    except Exception:
        pass
    print("# Login {0} successfully".format(account))



    driver.get("https://xg.hit.edu.cn/zhxy-xgzs/xg_mobile/xsTwsb")
    time.sleep(2)
    driver.execute_script("add()")
    time.sleep(2)
    try:
        alert = driver.switch_to.alert
        alert.accept()
    except Exception:
        pass
    print("# Add one item")

    js1 = """
            var data = [];
            data = {
                id :  twxx.id,
                sdid1   : twxx.sdid1 ,
                tw1 : 36.""" + str(random.choice([3,4,5,6,7])) + """ ,
                fr1 : 0 ,
                bs : "1"
            }
        
        $.ajax({
            url  : "/zhxy-xgzs/xg_mobile/xsTwsb/updateTwsb",
            type : "POST",
            data : {info:JSON.stringify({data : data})},
            dataType : "json",
            success:function(result){
                if(result.isSuccess){
                    $.toast("成功");
                    getXsjbxx();
                    getTwsb();
                }else{
                    $.toptip(result.msg);
                }
            },
            error : function(){
                $.toptip("保存体温信息失败");
            }
        });
    """

    js2 = """
            var data = [];
            data = {
                id :  twxx.id,
                sdid2   : twxx.sdid2 ,
                tw2 : 36.""" + str(random.choice([3,4,5,6,7])) + """ ,
                fr2 : 0 ,
                bs : "2"
            }
        
        $.ajax({
            url  : "/zhxy-xgzs/xg_mobile/xsTwsb/updateTwsb",
            type : "POST",
            data : {info:JSON.stringify({data : data})},
            dataType : "json",
            success:function(result){
                if(result.isSuccess){
                    $.toast("成功");
                    getXsjbxx();
                    getTwsb();
                }else{
                    $.toptip(result.msg);
                }
            },
            error : function(){
                $.toptip("保存体温信息失败");
            }
        });
    """
    try:
        driver.execute_script(js1)
        time.sleep(2)
        print("# Temperature 1 uploaded")
        driver.execute_script(js2)
        time.sleep(2)
        print("# Temperature 2 uploaded")
    except Exception:
        print("# [ERROR] Temperature upload failed")

    # 每日填报

    # driver.find_element_by_css_selector("div.right_btn").click()
    # edit_btn = None
    # for elem in driver.find_elements_by_css_selector("div"):
    #     if elem.text == "修改":
    #         edit_btn = elem
    #         break
    # edit_btn.parentt.get_attribute("innerHTML")
    js = """
    $.ajax({
            url : "/zhxy-xgzs/xg_mobile/xs/getYqxxList", 
            type : "Post",
            dataType : "json", 
            success : function(result) { 
                if (!result.isSuccess) {
                    return -1
                } else { 
                    var data = result.module.data;
                    //return data[0]
                    $("<div id='info'>" + data[0].id + "</div>").appendTo($("body"));       
                    }
                }
            })

    """
    driver.execute_script(js)
    time.sleep(2)

    driver.get('https://xg.hit.edu.cn/zhxy-xgzs/xg_mobile/xs/editYqxx?id=' + driver.find_element_by_id("info").text + '&zt=00')
    print("# ID got")
  
    driver.find_element_by_css_selector("#txfscheckbox").click()

    driver.execute_script("save()")


    print("# Information uploaded")

    

    time.sleep(2)
    