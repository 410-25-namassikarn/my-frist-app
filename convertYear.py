import streamlit as dm
dm.title("แอปพลิเคชั่นแปลงปี พ.ศ. เป็น ค.ศ.")

bl_year=dm.number_input("กรอกปี พ.ศ. ที่ต้องการแปลง",value=2569)
gl_year=bl_year-543
dm.header(f"ปี ค.ศ. คือ : {gl_year}")
