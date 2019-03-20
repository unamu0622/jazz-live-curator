from django.db import models


class Club(models.Model):
    club_name = models.CharField('店', max_length=200)
    url = models.CharField('URL', max_length=200)
    address = models.CharField('住所', max_length=200)
    phone_number = models.CharField('電話番号', max_length=200)
    email = models.EmailField('Email')

    def __str__(self):
        return self.club_name


class Player(models.Model):
    player_name = models.CharField('プレイヤー', max_length=200)
    instrument = models.CharField('楽器', max_length=200)

    def __str__(self):
        return self.player_name


class Live(models.Model):
    live_name = models.CharField('ライブ', max_length=200)
    club = models.ForeignKey(
        Club, on_delete=models.PROTECT, verbose_name="クラブ")
    player = models.ManyToManyField(
        Player, verbose_name="プレイヤー")
    open_time = models.DateTimeField('オープン')
    start_time = models.DateTimeField('スタート')

    def __str__(self):
        return self.live_name
