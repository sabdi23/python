from television import Television


class TestTelevision:

    def setup_method(self):
        self.tv = Television()

    def teardown_method(self):
        del self.tv

    def test_init(self):
        assert self.tv.__str__() == "Power = False, Channel = 0, Volume = 0"

    def test_power(self):
        self.tv.power()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 0"

        self.tv.power()
        assert self.tv.__str__() == "Power = False, Channel = 0, Volume = 0"

    def test_mute(self):
        self.tv.power()
        self.tv.volume_up()
        self.tv.mute()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 0"

        self.tv.mute()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 1"

        tv2 = Television()
        tv2.mute()
        assert tv2.__str__() == "Power = False, Channel = 0, Volume = 0"

        tv2.mute()
        assert tv2.__str__() == "Power = False, Channel = 0, Volume = 0"

    def test_channel_up(self):
        tv1 = Television()
        tv1.channel_up()
        assert tv1.__str__() == "Power = False, Channel = 0, Volume = 0"

        tv2 = Television()
        tv2.power()
        tv2.channel_up()
        assert tv2.__str__() == "Power = True, Channel = 1, Volume = 0"

        tv3 = Television()
        tv3.power()
        tv3.channel_up()
        tv3.channel_up()
        tv3.channel_up()
        tv3.channel_up()
        assert tv3.__str__() == "Power = True, Channel = 0, Volume = 0"

    def test_channel_down(self):
        tv1 = Television()
        tv1.channel_down()
        assert tv1.__str__() == "Power = False, Channel = 0, Volume = 0"

        tv2 = Television()
        tv2.power()
        tv2.channel_down()
        assert tv2.__str__() == "Power = True, Channel = 3, Volume = 0"

    def test_volume_up(self):
        tv1 = Television()
        tv1.volume_up()
        assert tv1.__str__() == "Power = False, Channel = 0, Volume = 0"

        tv2 = Television()
        tv2.power()
        tv2.volume_up()
        assert tv2.__str__() == "Power = True, Channel = 0, Volume = 1"

        tv3 = Television()
        tv3.power()
        tv3.volume_up()
        tv3.mute()
        tv3.volume_up()
        assert tv3.__str__() == "Power = True, Channel = 0, Volume = 2"

        tv4 = Television()
        tv4.power()
        tv4.volume_up()
        tv4.volume_up()
        tv4.volume_up()
        assert tv4.__str__() == "Power = True, Channel = 0, Volume = 2"

    def test_volume_down(self):
        tv1 = Television()
        tv1.volume_down()
        assert tv1.__str__() == "Power = False, Channel = 0, Volume = 0"

        tv2 = Television()
        tv2.power()
        tv2.volume_up()
        tv2.volume_up()
        tv2.volume_down()
        assert tv2.__str__() == "Power = True, Channel = 0, Volume = 1"

        tv3 = Television()
        tv3.power()
        tv3.volume_up()
        tv3.volume_up()
        tv3.mute()
        tv3.volume_down()
        assert tv3.__str__() == "Power = True, Channel = 0, Volume = 1"

        tv4 = Television()
        tv4.power()
        tv4.volume_down()
        assert tv4.__str__() == "Power = True, Channel = 0, Volume = 0"