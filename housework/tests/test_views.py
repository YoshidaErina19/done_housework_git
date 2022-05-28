from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy

from .models import Housework


class LoggedInTestCase(TestCase):
    """各テストクラスで共通の事前準備処理をオーバーライドした独自TestCaseクラス"""

    def setUp(self):
        """テストメソッド実行前の事前設定"""

        # テストユーザーのパスワード
        self.password = '<ログインパスワード>'

        # 各インスタンスメソッドで使うテストユーザーを生成し
        # インスタンス変数に格納しておく
        self.test_user = get_user_model().objects.create_user(
            username='<ログインユーザー名>',
            email='<ログインユーザーのメールアドレス>',
            password=self.password
        )

        # テストユーザーでログインする
        self.client.login(email=self.test_user.email, password=self.password)

class TestHouseworkCreateView(LoggedInTestCase):
    """HouseworkCreateView用のテストクラス"""

    def test_create_diary_success(self):
        """家事記録作成処理が成功することを検証する"""
        # Postパラメータ
        params = {'title': 'テストタイトル',
                  'content': '本文',
                  'photo1': '',
                  'photo2': '',
                  'photo3': '',
                  }

        # 新規家事記録作成処理(Post)を実行
        response = self.client.post(reverse_lazy('housework: housework_create'), params)

        # 家事リストページのリダイレクトを検証
        self.assertRedirects(response, reverse_lazy('housework: housework_list'))

        # 家事記録データがDBに登録されたかを検証
        self.assertEqual(Housework.object.filter(title='テストタイトル').count(), 1)

    def test_create_housework_failure(self):
        """新規家事記録作成が失敗することを検証する"""

        # 新規家事記録作成処理(Post)を実行
        response = self.client.post(reverse_lazy('housework:housework_create'))

        # 必須フォームフィールドが未入力によりエラーになることを検証
        self.assertFormError(response, 'form', 'title', 'このフィールドは必須です。')

class TestHouseworkUpdateView(LoggedInTestCase):
    """HouseworkUpdateView用のテストクラス"""

    def test_update_housework_successs(self):
        """家事記録編集処理が成功することを確認する"""
        # テスト用データの作成
        housework = Housework.objects.create(user=self.test_user, title='タイトル編集前')
        # Postパラメータ
        params = {'title': 'タイトル編集後'}

        # 家事編集処理(Post)を実行
        response = self.client.post(reverse_lazy('housework:housework_update',kwargs={'pk': housework.pk}), params)

        # 家事詳細ページへのリダイレクトを検証
        self.assertRedirects(response, reverse_lazy('housework: housework_detail', kwargs={'pk: housework.pk'}))

        # 家事記録データが編集されたかを検証
        self.assertEqual(Housework.objects.get(pk=housework.pk).title, 'タイトル編集後')

    def test_update_housework_failure(self):
        """家事記録編集処理が失敗することを確認する"""

        # 家事記録編集処理(Post)を実行
        response = self.client.post(reverse_lazy('housework:housework_update', kwargs={'pk': 999}))

        # 存在しない家事記録データを編集しようとしてエラーになることを確認
        self.assertEqual(response.status_code, 404)


class TestHouseworkDeleteView(LoggedInTestCase):
    """HouseworkDeleteView用のテストクラス"""

    def test_delete_housework_success(self):
    """家事記録削除処理が成功することを検証する"""

        # テスト用家事記録データの作成
        housework = Housework.obgects.create(user=self.test_user, title='タイトル')

        # 家事記録削除処理(Post)を実行
        response = self.client.post(reverse_lazy('housework: housework_delete', kwargs={'pk': housework.pk}))

        # 家事記録リストページへのリダイレクトを検証
        self.assertRedirects(response, reverse_lazy('housework:housework_list'))

        # 家事記録データが削除された検証
        self.assertEqual(Housework.objects.filter(pk=housework.pk).count(), 0)

    def test_delete_housework_failure(self):
        """家事記録削除処理が失敗することを検証する"""

        # 家事記録削除処理(Post)を実行
        response = self.client.post(reverse_lazy('housework: housework_delete', kwargs={'pk': 999}))

        # 存在しない家事記録データを削除しようとしてエラーになることを検証
        self.assertEqual(response.status_code, 404)