from django import forms
from django.core.mail import EmailMessage
from .models import Housework

class InquiryForm(forms.Form):
    name = forms.CharField(label='お名前',max_length=30)
    email = forms.EmailField(label='メールアドレス')
    title = forms.CharField(label='タイトル',max_length=30)
    message = forms.CharField(label='メッセージ',widget=forms.Textarea)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control col=9'
        self.fields['name'].widget.attrs['placeholder'] = 'お名前をここに入力してください'

        self.fields['email'].widget.attrs['class'] = 'form-control col=11'
        self.fields['email'].widget.attrs['placeholder'] = 'メールアドレスをここに入力してください'

        self.fields['title'].widget.attrs['class'] = 'form-control col=11'
        self.fields['title'].widget.attrs['placeholder'] = 'タイトルをここに入力してください'

        self.fields['message'].widget.attrs['class'] = 'form-control col=12'
        self.fields['message'].widget.attrs['placeholder'] = 'メッセージをここに入力してください'

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        title = self.cleaned_data['title']
        message = self.cleaned_data['message']

        subject = f'お問い合わせ {title}'
        message = f'送信者:　{name}\nメールアドレス: {email}\nタイトル: {title}\nメッセージ: {message}'
        from_email = 'admin@example.com'
        to_list = [
            'test@example.com'
        ]
        cc_list = [
            email
        ]

        message = EmailMessage(subject=subject,body=message,from_email=from_email,to=to_list,cc=cc_list)
        message.send()


class HouseworkCreateForm(forms.ModelForm):
    class Meta:
        model = Housework
        fields = ('title', 'content', 'bought_items','photo1', 'photo2', 'photo3',)
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'