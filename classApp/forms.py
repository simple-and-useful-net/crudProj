
from django import forms
from .models import PersonalDataModel
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


class MultiEmailField(forms.CharField):
    def __init__(self, *args, **kwargs):

        # self.choices = kwargs.pop('choices')
        super().__init__(*args, **kwargs)
        pass

    def to_python(self, value):
        """Normalize data to a list of strings."""
        # Return an empty list if no input was given.
        # if not value:
        #     return []
        # return value.split(",")
        return "abcd"
    
    def validate(self, value):
        """Check if value consists only of valid emails."""
        # Use the parent's handling of required fields, etc.
        super().validate(value)
        for email in value:
            validate_email(email)


class TestField(forms.MultipleChoiceField):

    def __init__(self, min_length=None, *args, **kwargs):
        self.min_length = min_length
        super().__init__(*args, **kwargs)    

    def to_python(self, value):
        print("to_python in ", value)
        """Normalize data to a list of strings."""

        # Return an empty list if no input was given.
        # if not value:
        #     return []
        # return value.split(",")
        return value

    def validate(self, value):
        print("validate in ", value)
        super().validate(value)

        # if not value.isalnum():
        #     raise ValidationError("This field must contain only alphanumeric characters.")

        # if self.min_length is not None and len(value) < self.min_length:
        #     raise ValidationError(f"This field must be at least {self.min_length} characters long.")

    def clean(self, value):
        print("clean in ", value)
        return str(value)
        # if not value:
        #     raise forms.ValidationError('Enter at least one e-mail address.')
        # emails = value.split(',')
        # for email in emails:
        #     if not is_valid_email(email):
        #         raise forms.ValidationError('%s is not a valid e-mail address.' % email)
        # return emails


class PersonalDataForm(forms.ModelForm):

    FOOD_CHOICES = [
        ('ラーメン', 'ラーメン'),
        ('寿司', '寿司'),
        ('カレー', 'カレー'),
    ]
    HOBBY_CHOICES = [
        ('音楽', '音楽'),
        ('映画', '映画'),
        ('アウトドア', 'アウトドア'),
    ]
    LABELS={
            "id":       "ID",
            "name":     "名前",
            "tel":      "電話番号",
            "email":    "メール",
            "sex":      "性別",
            "prefecture":"都道府県",
            "hobby":    "趣味",
            "food":     "食べ物",
    }


    food        = forms.MultipleChoiceField(choices=FOOD_CHOICES )
    hobby       = forms.MultipleChoiceField(choices=HOBBY_CHOICES, widget=forms.CheckboxSelectMultiple() )
    # hobby     = TestField(choices=HOBBY_CHOICES, widget=forms.CheckboxSelectMultiple(), label="Alphanumeric Field")
    # hobby2      = MultiEmailField(widget=forms.CharField(), label='趣味ABC')

    class Meta:
        model = PersonalDataModel
        
        # 個別に指定ができます
        # fields = ["name", "email", "sex", "prefecture", "hobby","food"]
        fields = "__all__"

        # フォームページに出力される名称
        # labels={
        #     "name":"名前",
        #     "sex":"性別",
        #     "prefecture":"都道府県",
        # }

        widgets = {
            'sex':      forms.RadioSelect(),
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # すべてのフィールドを指定
        for field_name, field in self.fields.items():
            field.required = False  # フィールドのrequired属性をFalseに設定
            field.label = PersonalDataForm.LABELS[field_name]

            if not field_name in ["sex","hobby"]:
                field.widget.attrs['class'] = 'form-control'

        # フィールドを指定して設定
        self.fields["name"].required = True
        self.fields['name'].widget.attrs['placeholder'] = '名前を入力してください'

    # モデルに保存
    def save(self, commit=True):

        instance = super(PersonalDataForm, self).save(commit=False)
        
        # フォームデータを変更
        # instance.memo = instance.memo + 'New Value'  # フィールド名と新しい値を指定

        # instance.categories.set(self.cleaned_data['categories'])
        # 選択されたカテゴリをモデルに関連付ける
        hobby10 = self.cleaned_data.get('hobby10')

        if commit:
            instance.save()
        return instance



    # 入力領域の個別チェックを行う場合はここでチェックする
    def clean_hobby10(self):
        data = self.cleaned_data.get('hobby10')
        return data        
    

    # すべての入力項目のチェックをしたい場合に使用
    # return時には「return self.cleaned_data」を返却が必要
    def clean( self ):
        # self.cleaned_data["hobby"]="abcdef"
        data1 = self.cleaned_data.get('hobby')
        data2 = self.cleaned_data.get('food')
        print(data1, data2)

        return self.cleaned_data
    



        
