from django import forms
from . import models
#定义一个类 => 一个表单
class ContactForm(forms.Form):
    #一个属性就是一个表单元素
    #forms.CharFiled => 字段类型
    #Label => 参数
    #widgets => 小部件
    """
    label => 设置标题（默认： 属性的名臣）
    required => True(默认必填项）
    min_length = > 设置内容的最短长度
    error_messages => 设置错误提示信息 =》 后端验证errors信息
    """
    subject = forms.CharField(label="主题", min_length=9, required=True, initial="Django-Form", error_messages={"min_length":"最少为9个字符","required":"主题是必填项"})    #CharField指文本框
    message = forms.CharField(label="内容", widget=forms.Textarea(attrs={"name":"abc", "class":"clsa", "style":"color:red;font-size:20px;","col":20}))
    sender = forms.EmailField(label="发送人")
    cc_myself = forms.BooleanField(label="抄送")
    #密码字段
    password = forms.CharField(label="密码", widget=forms.PasswordInput)
    #单radio值为字符串
    gender = forms.fields.ChoiceField(
        choices=((1, "男"),(2, "女"),(3, "保密")),
        label="性别",
        initial = 3,
        widget=forms.widgets.RadioSelect()
    )
    #下拉选择
    hobby = forms.fields.ChoiceField(
        choices=((1, "篮球"),(2, "足球"),(3, "排球")),
        label="爱好",
        initial=[1, 3],
        widget=forms.widgets.SelectMultiple()
    )
    #单选checkbox
    keep = forms.fields.ChoiceField(
        label="是否记住密码",
        initial="checked",
        widget=forms.widgets.CheckboxInput()
    )
    #多选checkbox
    hobby3 = forms.fields.MultipleChoiceField(
        choices=((1, "篮球"),(2, "足球"),(3, "排球")),
        label="爱好",
        initial=[1, 3],
        widget=forms.widgets.CheckboxSelectMultiple()
    )

class RegisterForm(forms.ModelForm):
    """
    注册表单
    因为Model中的元素默认是会把密码显示出来的，所以在这里重新定义一个password
    """
    password = forms.CharField(label="输入密码", max_length=18, widget=forms.PasswordInput)
    password2 = forms.CharField(label="确认密码", max_length=18, widget=forms.PasswordInput)
    class Meta:
        model = models.UserInfo
        #将model UserInfo中的字段生成到表单
        #exclude表示排除哪个字段，fields表示包含哪个字段，两个选项必须选其一
        #exclude = ()
        fields = ('username', 'password')

    def clean_username(self):
        """
        对username字段做检查用户名是否已经被注册
        注意字段一定要有返回值
        """
        #self.cleaned_data["username"] => 获取表单提交的username数据
        users = models.UserInfo.objects.filter(username=self.cleaned_data["username"])
        if not users:
            return self.cleaned_data["username"]
        else:
            raise forms.ValidationError("该用户已经被使用")

    def clean(self):
        """
        验证两次输入的密码是否一致
        对整个表单验证时，不需要返回值
        """
        if self.cleaned_data["password"] != self.cleaned_data["password2"]:
            raise forms.ValidationError("密码不一致!")


class LoginForm(forms.ModelForm):
    """
    登录表单
    """
    password = forms.CharField(label="密码", max_length=30, widget=forms.PasswordInput(attrs={"size": 20,}))
    def clean_username(self):
        user = models.UserInfo.objects.filter(username_iexact=self.cleaned_data["username"])
        if not user:
            raise forms.ValidationError("用户不存在")
        else:
            return self.cleaned_data["username"]

    class Meta:
        #配置用
        model = models.UserInfo    #对应的Model中的类
        exclude = ()