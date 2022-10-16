import re

from flask import Flask, render_template, request,Markup
from flask_wtf import FlaskForm
from flaskext.markdown import Markdown
from wtforms import SubmitField, TextAreaField


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main():
    if request.method == "POST" and request.form['action'] == 'button_sub':
        a_z=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        Plain_text = request.form.get("Plain_text")
        key = request.form.get("key")
        JorQ = request.form.get("JorQ")
        # print(Plain_text)
        # print(key)
        # print(JorQ)
        
        Plain_text_cut=re.findall(r"[a-z]",(Plain_text.lower()))
        Plain_text_cut=Plain_text_toP_lain_text(Plain_text_cut)

        key_table=create_key_table(key.lower(),a_z,JorQ.lower())

        Cipher_Text=encryption(Plain_text_cut,key_table)
        
        return render_template("index.html",Cipher_Text=Cipher_Text.upper())

    return render_template("index.html")

def create_key_table(key,a_z,JorQ): 
    rows, cols = (5, 5)
    arr = [[0 for i in range(cols)] for j in range(rows)]
    Round = 0
    
    key=list(key)
    a_z.remove(JorQ)
    
    for x in key:
        a_z.remove(x)

    for i in range(rows):
        for j in range(cols):
            
            if Round <len(key):
                Round_key= Round+1
                arr[i][j]=key[Round]
            
            if Round >=len(key):  
                arr[i][j]=a_z[Round-Round_key]
            Round+=1
    
    return (arr)

def encryption(Plain_text_cut,key_table):
    arr2 = [[0 for i in range(2)] for j in range(len(Plain_text_cut))]
    for x in range(len(Plain_text_cut)):
        for i in range(5):
            for j in range(5):
                if key_table[i][j] ==Plain_text_cut[x] :
                    arr2[x][0] =i
                    arr2[x][1] =j
    
    print(arr2)
    for x in range(len(Plain_text_cut)):
        if x%2 ==1:
            if arr2[x][1] == arr2[x-1][1]:
                arr2[x][0] =arr2[x][0] +1
                if  arr2[x][0] >=5:
                    arr2[x][0] =0
                arr2[x-1][0] =arr2[x-1][0] +1
                if  arr2[x-1][0] >=5:
                    arr2[x-1][0] =0
                # print("คู่แนวตั้ง")     
            elif arr2[x][0] == arr2[x-1][0]:
                arr2[x][1] =arr2[x][1] +1
                if  arr2[x][1] >=5:
                    arr2[x][1] =0
                arr2[x-1][1] =arr2[x-1][1] +1
                if  arr2[x-1][1] >=5:
                    arr2[x-1][1] =0
                # print("คู่แนวนอน")
            else :
                stay=arr2[x-1][1]
                arr2[x-1][1]=arr2[x][1]
                arr2[x][1] =stay
                # print("คู่แนวทแยง")
    
    # text="".join(arr2)
    text=""
    for x in range(len(arr2)):
        text+=(str(key_table[arr2[x][0]][arr2[x][1]]))
    return(text)

def Plain_text_toP_lain_text(Plain_text_cut):
    Plain_text_arr = []

    for x in range(len(Plain_text_cut)):
        if Plain_text_cut[x] ==Plain_text_cut[x-1]:
            Plain_text_arr.append("x")
        Plain_text_arr.append(Plain_text_cut[x])
    if len(Plain_text_arr)%2 == 1:
        Plain_text_arr.append("x")

    return(Plain_text_arr)



if __name__ == '__main__':
    app.debug = True
    app.run(debug=True)
    # app.run(host='0.0.0.0' , port=80)


# Plain_text="Why, don’t you?"
# key="keyword"
# JorQ='J'

# a_z=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Plain_text_cut=re.findall(r"[a-z]",(Plain_text.lower()))
# Plain_text_cut=Plain_text_toP_lain_text(Plain_text_cut)
# # print(Plain_text_cut)

# key_table=create_key_table(key.lower(),a_z,JorQ.lower())
# # print(key_table)

# Cipher_Text=encryption(Plain_text_cut,key_table)
# print(Cipher_Text)

