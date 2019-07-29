from django import forms
#定义一个类 => 一个表单
class ContactForm(forms.Form):
    #一个属性就是一个表单元素
    subject = forms.CharField(label="主题")    #CharField指文本框
    message = forms.CharField(label="内容", widget=forms.Textarea(attrs={"name":"abc", "class":"clsa", "style":"color:red;font-size:20px;"}))
    sender = forms.EmailField(label="发送人")
