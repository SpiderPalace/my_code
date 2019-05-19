from selenium import webdriver
import time
import random

driver = webdriver.Chrome()
# driver = webdriver.safari()
driver.get('http://passport2.chaoxing.com/login?fid=&refer=http://i.mooc.chaoxing.com')

time.sleep(random.random() * 3)

# 点击选择学校的按钮
xuexiao = driver.find_element_by_xpath('//*[@id="selectSchoolA"]')
xuexiao.click()
time.sleep(random.random() * 3)

# 点击河南
henan = driver.find_element_by_xpath('//*[@id="14"]')
henan.click()
time.sleep(random.random() * 5)

# 点击洛阳理工
louyang = driver.find_element_by_xpath('//*[@id="1283"]')
louyang.click()
time.sleep(random.random())

# 输入账号
ID = driver.find_element_by_xpath('//*[@id="unameId"]')
number = input("请输入账号：")
ID.send_keys(number)

# 输入密码
password = driver.find_element_by_xpath('//*[@id="passwordId"]')
password_number = input('请输入密码：')
password.send_keys(password_number)

# 输入验证码
yan_zheng_ma = input("请根据图片输入验证码:")
yang_zheng = driver.find_element_by_xpath('//*[@id="numcode"]')
yang_zheng.send_keys(yan_zheng_ma)

# 点击登录按钮
login = driver.find_element_by_xpath('//*[@id="form"]/table/tbody/tr[7]/td[2]/label/input').click()

# 得到慕课网址
get_url = 'https://mooc1-2.chaoxing.com/mycourse/studentstudy?chapterId=127067864&courseId=203379033&clazzid=6687211&enc=94d124749462f69967972f331c3c0040'
driver.get(get_url)
time.sleep(5)

# 遍历所有的章节
k = 0

# 得到所有章节
units = driver.find_elements_by_xpath('//*[@id="coursetree"]/div')
all1 = len(units)

for i in range(len(units)):
    try:
        driver.get(get_url)
        time.sleep(random.random() * 3)
        
        # 切换到iframe的html里面
        driver.switch_to.frame('iframe')
        time.sleep(random.random() * 4)

        # 切换到下面的iframe里
        try:
            driver.switch_to.frame(driver.find_element_by_xpath('//body/div/div/p/div/iframe'))
        except:
            driver.switch_to.frame(driver.find_element_by_xpath('//body/div/div/p/span/div/iframe'))

        time.sleep(random.random() * 5)

        # 切换到公网
        try:
            driver.find_element_by_xpath('//*[@id="coursetree"]/div[' + str(i + 1) + ']').click()
        except:
            driver.find_element_by_xpath('//*[@id="coursetree"]/div[' + str(i + 1) + ']/div').click()

        time.sleep(random.random() * 3)

        # 找到播放按钮并点击
        try:
            button = driver.find_element_by_xpath('//*[@id="reader"]')
            button.click()
        except:
            driver.find_element_by_xpath('//*[@id="dct2"]').click()
            driver.find_element_by_xpath('//*[@id="reader"]').click()

        time.sleep(random.random() * 3)

        # 找到总时间
        time_all = driver.find_element_by_xpath('//*[@id="video"]/div[4]/div[4]/span[2]').text
        print('正在播放第{}个， 时长是{}，一共有{}个， 完成度是{}'.format(k + 1, time_all, all1, k / all1))
        time.sleep(random.random() * 10)

        try:
            driver.find_element_by_xpath('//*[@id="video"]/div[4]/div[8]/span').click()
            driver.find_element_by_xpath('//*[@id="video"]/div[4]/div[8]/div/ul/li[3]/span[1]').click()
        except:
            pass

        # 找到快进按钮
        try:
            buttton2 = driver.find_element_by_xpath('//*[@id="video"]/div[4]/div[1]/button')
            buttton2.click()
            time.sleep(random.random())
            buttton2.click()
            time.sleep(random.random())
            buttton2.click()
            time.sleep(random.random())
            time.sleep(3)
        except:
            pass

        # 找到静音按钮
        time.sleep(3)
        try:

            slience = driver.find_element_by_css_selector(
                '#video > div.vjs-control-bar > div.vjs-volume-panel.vjs-control.vjs-volume-panel-vertical > button > span.vjs-icon-placeholder')
            slience.click()
            silence = driver.find_element_by_xpath('//*[@id="video"]/div[4]/div[6]')
            silence.click()
            time.sleep(6)
        except:
            pass

        n = 1
        while True:

            # 当网络不可用时  点击公网
            try:
                driver.find_element_by_xpath('//*[@id="vjserrdisplay-1035"]/ul/li[2]/label').click()
            except:
                pass

            try:
                # 找到视频中出现的答题位置
                if driver.find_element_by_xpath('//body/div[4]/div/div[7]/span/div/div'):

                    # 找到选择题
                    button3 = driver.find_elements_by_xpath('//body/div[4]/div/div[7]/span/div/div/ul/li')
                    # print("button3{}", button3)
                    while driver.find_element_by_xpath('//body/div[4]/div/div[7]/span/div/div'):
                        # print(1)
                        # 对选项进行遍历
                        for button1 in button3:
                            button1 = button1.find_element_by_xpath('label')
                            # print("button1{}", button1)
                            button1.click()
                            time.sleep(random.random() * 3)

                            # 点击提交按钮
                            button5 = driver.find_element_by_xpath('//body/div[4]/div/div[7]/span/div/div/div[2]')
                            # print("button5{}", button5)
                            button5.click()
                            time.sleep(random.random() * 3)
                            if driver.switch_to.alert():
                                al = driver.switch_to.alert()
                                al.accept()
                                time.sleep(random.random())
                            if not driver.find_element_by_xpath('//body/div[4]/div/div[7]/span/div/div'):
                                # print("答题完成")
                                break

            except Exception as e:
                # print("未找到答题位置")
                time.sleep(random.random() * 3)

            try:
                # 找到重播按钮
                rename = driver.find_element_by_xpath('//*[@id="video"]/div[4]/button[1]').get_attribute('title')
                if rename == '重播':
                    break
            except Exception as e:
                time.sleep(random.random() * 3)

        t = random.random() * 3
        time.sleep(t)

        # 切换到上一个iframe
        driver.switch_to_default.content()
        time.sleep(random.random())

        driver.switch_to_default.content()
        time.sleep(random.random())

        k += 1
    except Exception as e:
        print("error" + str(i + 1))
        k += 1
        continue
