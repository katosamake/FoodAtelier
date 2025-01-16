import uuid
from django.db import models
from django.utils import timezone

#ラベル編集①
class LabelTitle(models.Model):
    #ラベルタイトルコード
    label_title_code = models.CharField(max_length=4)
    #ラベルタイトル名
    label_title_name = models.TextField(max_length=15)

    def __str__(self):
        return self.label_title_code


#ラベル編集②
class LabelDetail(models.Model):
    #ラベルタイトルコード
    label_title_code = models.ForeignKey(LabelTitle, on_delete=models.CASCADE)
    #ラベル詳細コード   
    label_detail_code = models.CharField(max_length=6)
    #ラベル詳細名
    label_detail_name = models.TextField(max_length=10)

    def __str__(self):
        return self.label_detail_name


#入力フォーム
class Record(models.Model):
    #料理名
    food_name = models.CharField(max_length=20)

    #はじめて作った日
    first_date = models.DateTimeField(default=timezone.now)

    #画像
    picture = models.ImageField(
        upload_to="home/picture/", blank=True, null=True)

    #ラベルの選択
    # label_title1 → LabelDetailから label_title_code_id=1 のみ選べる
    label_title1 = models.ForeignKey(
        LabelDetail,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        limit_choices_to={'label_title_code_id': 1},
        related_name='records_title1'
    )

    # label_title2 → label_title_code_id=2 のみ
    label_title2 = models.ForeignKey(
        LabelDetail,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        limit_choices_to={'label_title_code_id': 2},
        related_name='records_title2'
    )

    # label_title3 → label_title_code_id=3 のみ
    label_title3 = models.ForeignKey(
        LabelDetail,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        limit_choices_to={'label_title_code_id': 3},
        related_name='records_title3'
    )

    # label_title4 → label_title_code_id=4 のみ
    label_title4 = models.ForeignKey(
        LabelDetail,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        limit_choices_to={'label_title_code_id': 4},
    related_name='records_title4'
)

    # label_title5 → label_title_code_id=5 のみ
    label_title5 = models.ForeignKey(
        LabelDetail,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        limit_choices_to={'label_title_code_id': 5},
    related_name='records_title5'
)

    # label_title6 → label_title_code_id=6 のみ
    label_title6 = models.ForeignKey(
        LabelDetail,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        limit_choices_to={'label_title_code_id': 6},
        related_name='records_title6'
)

    # label_title7 → label_title_code_id=7 のみ
    label_title7 = models.ForeignKey(
        LabelDetail,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        limit_choices_to={'label_title_code_id': 7},
    related_name='records_title7'
)

    # label_title8 → label_title_code_id=8 のみ
    label_title8 = models.ForeignKey(
        LabelDetail,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        limit_choices_to={'label_title_code_id': 8},
    related_name='records_title8'
)

    #メモ
    memo = models.TextField(max_length=100)

    def __str__(self):
        return self.food_name


