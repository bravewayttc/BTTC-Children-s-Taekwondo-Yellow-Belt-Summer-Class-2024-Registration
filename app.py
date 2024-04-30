import streamlit as st
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def selecttime(day_of_week,selected_date,i):
    if day_of_week in ["Monday", "Wednesday", "Friday"]:
        time_options = ["9:00-10:00", "13:00-14:00", "14:30-15:30"]
    elif day_of_week in ["Tuesday", "Thursday"]:
        time_options = ["10:00-11:00", "11:15-12:15", "14:00-15:00"]
    elif day_of_week == "Saturday":
        time_options = ["9:00-10:00", "11:15-12:15"]
    elif day_of_week == "Sunday":
        st.write("Please select a different date.")
        return
    else:
        time_options = ["9:00-10:00", "10:00-11:00", "11:15-12:15", "13:00-14:00", "14:30-15:30", "15:15-16:15",
                        "16:30-17:30"]
    i +=1
    # Time selection
    selected_time = st.selectbox("選擇時段", time_options, key=f"{selected_date}_{i}")
    return selected_time,i

def select_date(str):
    start_date = datetime(2024, 7, 15).date()
    end_date = datetime(2024, 8, 30).date()
    for i in range(10): # Limit the number of attempts to avoid infinite loops
        selected_date = st.date_input(f"{str}", datetime(2024, 7, 15), key=f"{str}_date_input_{i}")
        if selected_date >= start_date and selected_date <= end_date:
            day_of_week = selected_date.strftime("%A")
            if day_of_week in ["Monday", "Wednesday", "Friday","Tuesday", "Thursday","Saturday"]:
                break
            else:
                st.error("請再選擇一次，不要選擇星期日")
        else:
            st.error("Please select a date between 15/7 and 30/8.")

    # Determine the day of the week

    return day_of_week,selected_date

def send_email(parent_name, content_number, living_area, kid_name, kid_yeasold, kid_gender, lessons):
    # Set up the SMTP server and login.
    # Replace 'your_email@example.com' and 'your_password' with your actual email and password.
    # For Gmail, the server is 'smtp.gmail.com' and the port is 587.
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("hoyin99999@gmail.com", "Maulei41")
    #"bravewayttc.autoreply@gmail.com", "BTTCeway2024"
    # Create the email.
    msg = MIMEMultipart()
    msg['From'] = "hoyin99999@gmail.com"
    msg['To'] = "hoyin99999@gmail.com"
    msg['Subject'] = "育苗跆拳道訓練中心 兒童跆拳道黃帶暑期班2024 報名"

    # Compose the email body with the collected information.
    body = f"家長稱謂： {parent_name}\n" \
           f"聯絡電話： {content_number}\n" \
           f"居住地區：{living_area}\n" \
           f"小朋友姓名： {kid_name}\n" \
           f"小朋友姓名：' {kid_yeasold}\n" \
           f"小朋友性别： {kid_gender}\n" \
           f"上堂日子:\n" + "\n".join(lessons)

    msg.attach(MIMEText(body, 'plain'))

    # Send the email.
    server.send_message(msg)
    server.quit()

    st.success("Email sent successfully!")

def main():
    st.title("育苗跆拳道訓練中心 兒童跆拳道黃帶暑期班 2024")
    j = 0
    st.write(" \$1600/10堂，其後每堂加 \$100，包考試費用\n\n完成10堂後可報考黃帶晉升試\n\n成功考取黃帶將獲發證書\n\n6月15日前報讀全期九折")
    st.subheader("注意事項")
    st.write("如報名人數過多 ，本中心將以抽籤形式確認參加者名額。\n\n學員因病假、遲到或缺席者，即視作曠課，課堂均不得順延、退款或退換。\n\n跆拳道是一種以腿部動作為主之武術\n\n其主旨為崇禮，尚義，服從，忍耐四大原則，而經過嚴恪之訓線課程，可加強學員之紀律性,自發性和堅毅不屈之情神。\n\n經過一段指定時間之訓練後，學員可参加晉級試，合格後使可升级")
    st.subheader("上課地點")
    st.write("新界沙田源順圍28號都會廣場2009室")
    st.subheader("報名名單\n")
    parant_name = st.text_input("家長稱謂：")
    st.write(f"您的稱謂是{parant_name}")
    content_number = st.text_input("聯絡電話：")
    st.write(f"您的聯絡電話是{content_number}")
    living_area =st.text_input('居住地區：')
    st.write(f"您的居住地區是{living_area}")
    kid_name = st.text_input('小朋友姓名：')
    st.write(f"小朋友的姓名是{kid_name}")
    kid_yeasold = st.text_input('小朋友年齡：')
    st.write(f"小朋友的年齡是{kid_yeasold}")
    kid_gender = st.selectbox("小朋友性别：",("女","男"))
    st.write(f"小朋友的性别是{kid_gender}")
    lesson1_day,lesson1_date = select_date("第一堂日期(星期一至星期六)：")
    lesson1_time,j = selecttime(lesson1_day,lesson1_date,j)
    st.write(f"第二堂日期是{lesson1_date}，時段是{lesson1_time}")
    lesson2_day,lesson2_date = select_date("第二堂日期(星期一至星期六)：")
    lesson2_time,j = selecttime(lesson2_day,lesson2_date,j)
    st.write(f"第二堂日期是{lesson2_date}，時段是{lesson2_time}")
    lesson3_day, lesson3_date = select_date("第三堂日期(星期一至星期六)：")
    lesson3_time,j = selecttime(lesson3_day,lesson3_date,j)
    st.write(f"第三堂日期是{lesson3_date}，時段是{lesson3_time}")
    lesson4_day, lesson4_date = select_date("第四堂日期(星期一至星期六)：")
    lesson4_time,j = selecttime(lesson4_day,lesson4_date,j)
    st.write(f"第三堂日期是{lesson4_date}，時段是{lesson4_time}")
    lesson5_day, lesson5_date = select_date("第五堂日期(星期一至星期六)：")
    lesson5_time,j = selecttime(lesson5_day,lesson5_date,j)
    st.write(f"第五堂日期是{lesson5_date}，時段是{lesson5_time}")
    lesson6_day, lesson6_date = select_date("第六堂日期(星期一至星期六)：")
    lesson6_time,j = selecttime(lesson6_day,lesson6_date,j)
    st.write(f"第六堂日期是{lesson6_date}，時段是{lesson6_time}")
    lesson7_day, lesson7_date = select_date("第七堂日期(星期一至星期六)：")
    lesson7_time,j = selecttime(lesson7_day,lesson7_date,j)
    st.write(f"第七堂日期是{lesson7_date}，時段是{lesson7_time}")
    lesson8_day, lesson8_date = select_date("第八堂日期(星期一至星期六)：")
    lesson8_time,j = selecttime(lesson8_day,lesson8_date,j)
    st.write(f"第八堂日期是{lesson8_date}，時段是{lesson8_time}")
    lesson9_day, lesson9_date = select_date("第九堂日期(星期一至星期六)：")
    lesson9_time,j = selecttime(lesson9_day,lesson9_date,j)
    st.write(f"第九堂日期是{lesson9_date}，時段是{lesson9_time}")
    lesson10_day, lesson10_date = select_date("第十堂日期(星期一至星期六)：")
    lesson10_time,j = selecttime(lesson10_day,lesson10_date,j)
    st.write(f"第十堂日期是{lesson10_date}，時段是{lesson10_time}")


    # Submit button
    if st.button("Submit"):
        st.write()
        lessons = [
            f"Lesson 1: {lesson1_date} {lesson1_time}",
            f"Lesson 2: {lesson2_date} {lesson2_time}",
            f"Lesson 3: {lesson3_date} {lesson3_time}",
            f"Lesson 4: {lesson4_date} {lesson4_time}",
            f"Lesson 5: {lesson5_date} {lesson5_time}",
            f"Lesson 6: {lesson6_date} {lesson6_time}",
            f"Lesson 7: {lesson7_date} {lesson7_time}",
            f"Lesson 8: {lesson8_date} {lesson8_time}",
            f"Lesson 9: {lesson9_date} {lesson9_time}",
            f"Lesson 10: {lesson10_date} {lesson10_time}"
        ]
        send_email(parant_name, content_number, living_area, kid_name, kid_yeasold, kid_gender, lessons)

if __name__ == "__main__":
    main()
