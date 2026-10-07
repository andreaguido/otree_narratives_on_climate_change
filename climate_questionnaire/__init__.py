import random

from otree.api import *
from settings import SURVEY_LANGUAGE as LANGUAGE_CODE

doc = """
Narratives on Climate Change
"""

language = {"en": False, "fr": False, "vi": False, LANGUAGE_CODE: True}
_ = lambda x: x[LANGUAGE_CODE]


def get_scale_action():
    return [
        [-2, _(dict(en="Not at all", fr="Pas du tout", vi="Không hề"))],
        [-1, _(dict(en="-1", fr="-1", vi="-1"))],
        [0, _(dict(en="Moderately", fr="Modérément", vi="Ở mức vừa phải"))],
        [1, _(dict(en="1", fr="1", vi="1"))],
        [2, _(dict(en="A great deal", fr="Énormément", vi="Rất nhiều"))]
    ]


def get_scale_policy():
    return [
        [-2, _(dict(en="Strongly oppose", fr="Fortement opposé(e)", vi="Hoàn toàn phản đối"))],
        [-1, _(dict(en="Somewhat oppose", fr="Plutôt opposé(e)", vi="Hơi phản đối"))],
        [0, _(dict(en="Neither support nor oppose", fr="Ni favorable ni opposé(e)", vi="Không phản đối cũng không ủng hộ"))],
        [1, _(dict(en="Somewhat support", fr="Plutôt favorable", vi="Hơi ủng hộ"))],
        [2, _(dict(en="Strongly support", fr="Fortement favorable", vi="Hoàn toàn ủng hộ"))]
    ]

def get_scale_certainty():
    return [
        [-2, _(dict(en="Very uncertain", fr="Très incertain", vi="Rất không chắc chắn"))],
        [-1, _(dict(en="Uncertain", fr="Incertain", vi="Không chắc chắn"))],
        [1, _(dict(en="Certain", fr="Certain", vi="Chắc chắn"))],
        [2, _(dict(en="Very certain", fr="Très certain", vi="Rất chắc chắn"))],
    ]

def get_scale_frequency_info():
    return [
            [5, _(dict(en="Daily", fr="Quotidiennement", vi="Hàng ngày"))],
            [4, _(dict(en="Twice per week", fr="Deux fois par semaine", vi="Hai lần mỗi tuần"))],
            [3, _(dict(en="Once per week", fr="Une fois par semaine", vi="Một lần mỗi tuần"))],
            [2, _(dict(en="Twice per month", fr="Deux fois par mois", vi="Hai lần mỗi tháng"))],
            [1, _(dict(en="Once per month", fr="Une fois par mois", vi="Một lần mỗi tháng"))],
            [0, _(dict(en="Never", fr="Jamais", vi="Không bao giờ"))]
        ]

def get_scale_expectations():
    return [
        [-2, _(dict(en="Very unlikely", fr="Très improbable", vi="Rất khó xảy ra"))],
        [-1, _(dict(en="Somewhat unlikely", fr="Plutôt improbable", vi="Hơi khó xảy ra"))],
        [1, _(dict(en="Somewhat likely", fr="Plutôt probable", vi="Hơi có khả năng xảy ra"))],
        [2, _(dict(en="Very likely", fr="Très probable", vi="Rất có khả năng xảy ra"))]
    ]

def get_scale_agreement():
    return [
        [-2, _(dict(en="Strongly disagree", fr="Fortement en désaccord", vi="Hoàn toàn không đồng ý"))],
        [-1, _(dict(en="Somewhat disagree", fr="Plutôt en désaccord", vi="Hơi không đồng ý"))],
        [0, _(dict(en="Neither agree nor disagree", fr="Ni d'accord ni en désaccord", vi="Không đồng ý cũng không phản đối"))],
        [1, _(dict(en="Somewhat agree", fr="Plutôt d'accord", vi="Hơi đồng ý"))],
        [2, _(dict(en="Strongly agree", fr="Fortement d'accord", vi="Hoàn toàn đồng ý"))]
    ]
def get_scale_income():
    return [
        [0, _(dict(en="From 0 to 5,000,000 VND", fr="De 0€ à 1 250€", vi="Từ 0 đến 5.000.000 VND"))],
        [1, _(dict(en="From 5,000,000 to 10,000,000 VND", fr="De 1 250€ à 2 000€", vi="Từ 5.000.000 đến 10.000.000 VND"))],
        [2, _(dict(en="From 10,000,000 to 15,000,000 VND", fr="De 2 000€ à 4 000€", vi="Từ 10.000.000 đến 15.000.000 VND"))],
        [3, _(dict(en="From 15,000,000 to 30,000,000 VND", fr="De 4 000€ à 6 000€", vi="Từ 15.000.000 đến 30.000.000 VND"))],
        [4, _(dict(en="From 30,000,000 to 45,000,000 VND", fr="De 6 000€ à 8 000€", vi="Từ 30.000.000 đến 45.000.000 VND"))],
        [5, _(dict(en="From 45,000,000 to 60,000,000 VND", fr="De 8 000€ à 12 500€", vi="Từ 45.000.000 đến 60.000.000 VND"))],
        [6, _(dict(en="More than 60,000,000 VND", fr="Plus de 12 500€", vi="Hơn 60.000.000 VND"))],
        [999, _(dict(en="I prefer not to say", fr="Je préfère ne pas répondre", vi="Tôi không muốn trả lời"))]
    ]
def get_scale_education():
    return [
        [0, _(dict(en="Primary or lower secondary education", fr="Primaire ou collège", vi="Giáo dục tiểu học hoặc trung học cơ sở"))],
        [1, _(dict(en="Upper secondary education", fr="Lycée (Baccalauréat)", vi="Giáo dục trung học phổ thông"))],
        [2, _(dict(en="Non-university post-secondary education", fr="Formation post-secondaire non universitaire", vi="Giáo dục sau trung học không thuộc đại học"))],
        [3, _(dict(en="Undergraduate education (bachelor)", fr="Licence (Bachelor)", vi="Giáo dục đại học (cử nhân)"))],
        [4, _(dict(en="Postgraduate education (Master or PhD)", fr="Master ou Doctorat", vi="Giáo dục sau đại học (Thạc sĩ hoặc Tiến sĩ)"))],
        [999, _(dict(en="I prefer not to say", fr="Je préfère ne pas répondre", vi="Tôi không muốn trả lời"))]
    ]
def get_options_bdm():
    return [
        ['A', _(dict(en='Option A', fr='Option A', vi="Lựa chọn A"))],
        ['B', _(dict(en='Option B', fr='Option B', vi="Lựa chọn B"))]
    ]
class C(BaseConstants):
    NAME_IN_URL = 'clquest'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    ROW_INDICES = [0, 1, 2, 3, 4, 5, 6] # rows of the MPL table (all 7 can be drawn, as in the lab sessions)
    AMOUNTS = [50, 1500, 3000, 5000, 10500, 14000, 17000] # amounts of the MPL table, in VND, as in the Vietnam lab sessions (set by A. Guido 15 Dec 2025, PPP from USD [0.01, 0.25, 0.5, 1, 1.5, 2, 2.5])

class Subsession(BaseSubsession):
    prolific = models.BooleanField()


def creating_session(subsession: Subsession):
    # store if it is a prolific session
    subsession.prolific = subsession.session.config.get("prolific", False)

    # define who arae the ones drawn for MPL
    import random
    players = subsession.get_players()

    # If there are fewer than 10 players but you still want max(…)
    k = min(10, len(players))

    # 1. randomly select 10 players (or fewer if session < 10)
    selected_players = random.sample(players, k=k)

    for p in players:
        p.is_selected = (p in selected_players)

    # 2. for each selected player, draw a random row of the MPL
    for p in selected_players:
        p.random_row = random.choice(C.ROW_INDICES)
        p.random_amount = C.AMOUNTS[p.random_row]
    #subsession.creating_session()

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    skip = models.BooleanField()

    # Narrative elicitation -----------
    climate_exists = models.BooleanField(
        choices=[
            [True, _(dict(en="Yes", fr="Oui", vi="Có"))],
            [False, _(dict(en="No", fr="Non", vi="Không"))]
        ],
        label=_(
            dict(
                en="Do you think climate change is a real phenomenon?",
                fr="Pensez-vous que le changement climatique soit un phénomène réel ?", vi="Bạn có nghĩ rằng biến đổi khí hậu là một hiện tượng có thật không?"
            )
        ),
        widget=widgets.RadioSelectHorizontal
    )
    narrative_elicitation = models.LongStringField(
        label=_(dict(
            en=(
                "In your opinion, what explains the facts described in the text before (such as the reported rise in global temperatures and more extreme weather events)? <br><br>"
                "Please describe the <b>causes</b> of the facts attributed to climate change, and <b>explain</b> how these causes contribute to these facts and might be connected to each other.  <br><br> "
                "Explain your reasoning in full sentences. "
                "There is no good or wrong answer, respond according to your sincere and personal opinion. <br> [min. 50 words]"),
            fr=("Selon vous, quelles sont les causes des faits décrits dans le texte précédent (comme la hausse des "
            "températures mondiales et l'augmentation des événements météorologiques extrêmes) ? <br><br>"
            "Veuillez décrire les <b>causes</b> des faits attribués au changement climatique, et "
            "<b>expliquer</b> comment ces causes contribuent à ces faits et pourraient être liées entre elles. <br><br> "
            "Expliquez votre raisonnement avec des phrases complètes. "
            "Il n'y a pas de bonne ou de mauvaise réponse, répondez selon votre opinion sincère et personnelle. <br> "
            "[min. 50 mots]"), vi="Theo bạn, nguyên nhân của các hiện tượng được miêu tả trong đoạn văn trước đó là gì? (chẳng hạn như các số liệu về mức tăng nhiệt độ trung bình toàn cầu và các hiện tượng thời tiết cực đoan)? <br><br>Vui lòng mô tả các <b>nguyên nhân</b> của những hiện tượng biến đổi khí hậu, và <b>giải thích</b> tại sao những nguyên nhân này góp phần tạo ra các hiện tượng đó, cũng như các nguyên nhân này có thể liên hệ với nhau như thế nào. <br><br> Hãy giải thích lập luận của bạn bằng các câu hoàn chỉnh. Không có câu trả lời đúng hay sai; hãy trả lời theo ý kiến cá nhân theo những gì bạn nghĩ của bạn. <br> [tối thiểu 50 từ]"
        ))
    )
    narrative_confidence = models.IntegerField(
        label=_(dict(
            en=(
                ""),
            fr=(""
                ""), vi=""
        ))
    )

    # Narrative sharing ---------------
    sharing_narrative = models.FloatField(
        label="",
        max=10
    )
    # One field per MPL row
    choice_1 = models.StringField(choices=get_options_bdm(), widget=widgets.RadioSelectHorizontal)
    choice_2 = models.StringField(choices=get_options_bdm(), widget=widgets.RadioSelectHorizontal)
    choice_3 = models.StringField(choices=get_options_bdm(), widget=widgets.RadioSelectHorizontal)
    choice_4 = models.StringField(choices=get_options_bdm(), widget=widgets.RadioSelectHorizontal)
    choice_5 = models.StringField(choices=get_options_bdm(), widget=widgets.RadioSelectHorizontal)
    choice_6 = models.StringField(choices=get_options_bdm(), widget=widgets.RadioSelectHorizontal)
    choice_7 = models.StringField(choices=get_options_bdm(), widget=widgets.RadioSelectHorizontal)

    is_selected = models.BooleanField(initial=False)
    random_row = models.IntegerField(initial=None)
    random_amount = models.FloatField(initial=None)
    payoff_mpl = models.FloatField()

    # Policy --------------------------
    policy_fight = models.IntegerField(
        choices=[
            [1, _(dict(en="Yes", fr="Oui", vi="Có"))],
            [0, _(dict(en="No", fr="Non", vi="Không"))],
            [-1, _(dict(en="I don't know/I do not want to answer", fr="Je ne sais pas / souhaite pas répondre", vi="Tôi không biết/Tôi không muốn trả lời"))]
        ],
        label=_(
            dict(
                en="In your opinion, do you think your country should fight climate change?",
                fr="Selon vous, votre pays doit-il lutter contre le changement climatique ?", vi="Theo bạn, đất nước bạn có nên đấu tranh chống biến đổi khí hậu không?"
            )
        ),
        widget=widgets.RadioSelectHorizontal
    )

    policy_narrative = models.LongStringField(
        label=_(dict(
            en=(""),
            fr=(""), vi=""
        ))
    )

    # Policy_question_certain
    confidence_policy = models.IntegerField(
        label=_(dict(
            en=(
                ""),
            fr=(""), vi=""
        )),
    )

    # Policy_expectations
    expectations_policy_economy = models.IntegerField(
        label=_(
            dict(
                en="<b>The solution I mentioned would have a positive effect on my country’s economy and employment</b>",
                fr="<b>La solution que j’ai mentionnée aurait un effet positif sur l’économie et l’emploi de mon pays</b>", vi="Giải pháp mà tôi đã nêu sẽ có tác động tích cực đến kinh tế và tình hình việc làm ở nước tôi."
            )
        ),
        choices = get_scale_agreement(),
        widget=widgets.RadioSelectHorizontal
    )
    expectations_policy_cc = models.IntegerField(
        label=_(
            dict(
                en="<b>The solution I mentioned would help limit and/or mitigate the consequences of climate change</b>",
                fr="<b>La solution que j’ai mentionnée aiderait à limiter et/ou atténuer les conséquences du changement climatique</b>", vi="Giải pháp mà tôi đã nêu sẽ giúp hạn chế và/hoặc giảm nhẹ các hậu quả của biến đổi khí hậu."
            )
        ),
        choices=get_scale_agreement(),
        widget=widgets.RadioSelectHorizontal
    )
    expectations_policy_household = models.IntegerField(
        label=_(
            dict(
                en="<b>My household will win or lose financially from the solution I mentioned</b>",
                fr="<b>Mon foyer gagnera ou perdra financièrement de la solution que j’ai mentionnée</b>", vi="Gia đình của tôi sẽ được lợi hoặc chịu thiệt về tài chính từ giải pháp mà tôi đã nêu."
            )
        ),
        choices=[
            [-2, _(dict(en="Lose a lot", fr="Perdre beaucoup", vi="Mất rất nhiều"))],
            [-1, _(dict(en="Lose", fr="Perdre", vi="Mất"))],
            [0, _(dict(en="Neither win or lose", fr="Ni gagner ni perdre", vi="Không lãi cũng không lỗ"))],
            [1, _(dict(en="Win", fr="Gagner", vi="Được lợi"))],
            [2, _(dict(en="Win a lot", fr="Gagner beaucoup", vi="Được lợi rất nhiều"))],
        ],
        widget=widgets.RadioSelectHorizontal
    )

    agreement_policy = models.IntegerField(
        label=_(
            dict(
                en="<b>Do you support or oppose the solution you provided?</b>",
                fr="<b>Êtes-vous favorable ou opposé(e) à la solution que vous avez fournie ?</b>", vi="Bạn ủng hộ hay phản đối giải pháp mà bạn đã đề xuất?"
            )
        ),
        choices=[
            [-2, _(dict(en="Strongly oppose", fr="Fortement opposé(e)", vi="Hoàn toàn phản đối"))],
            [-1, _(dict(en="Somewhat oppose", fr="Plutôt opposé(e)", vi="Hơi phản đối"))],
            [0, _(dict(en="Neither support nor oppose", fr="Ni favorable ni opposé(e)", vi="Không phản đối cũng không ủng hộ"))],
            [1, _(dict(en="Somewhat support", fr="Plutôt favorable", vi="Hơi ủng hộ"))],
            [2, _(dict(en="Strongly support", fr="Fortement favorable", vi="Hoàn toàn ủng hộ"))],
        ],
        widget=widgets.RadioSelectHorizontal
    )

    # Climate knowledge ---------------
    climate_knowledge = models.IntegerField(
        label=_(
            dict(
                en="How knowledgeable do you consider yourself about climate change?",
                fr="À quel point vous considérez-vous informé(e) sur le changement climatique ?", vi="Bạn đánh giá kiến thức về biến đổi khí hậu của mình như thế nào?",
            )
        ),
        choices=[
            [0, _(dict(en="Not at all", fr="Pas du tout", vi="Không hề"))],
            [1, _(dict(en="A little", fr="Un peu", vi="Một chút"))],
            [2, _(dict(en="Moderately", fr="Modérément", vi="Ở mức vừa phải"))],
            [3, _(dict(en="A lot", fr="Beaucoup", vi="Nhiều"))],
            [4, _(dict(en="A great deal", fr="Énormément", vi="Rất nhiều"))]
        ],
        widget=widgets.RadioSelectHorizontal,
    )
    rank_coal = models.IntegerField(
        label=_(dict(
            en="Rank of Coal-fired power station",
            fr="Classement de la centrale à charbon", vi="Xếp hạng của nhà máy điện than"
        )),
        choices=[1, 2, 3],
        widget=widgets.RadioSelectHorizontal
    )
    rank_gas = models.IntegerField(
        label=_(dict(
            en="Rank of Gas-fired power plant",
            fr="Classement de la centrale à gaz", vi="Xếp hạng của nhà máy điện khí"
        )),
        choices=[1, 2, 3],
        widget=widgets.RadioSelectHorizontal
    )
    rank_nuclear = models.IntegerField(
        label=_(dict(
            en="Rank of Nuclear power plant",
            fr="Classement de la centrale nucléaire", vi="Xếp hạng của nhà máy điện hạt nhân"
        )),
        choices=[1, 2, 3],
        widget=widgets.RadioSelectHorizontal
    )
    # Media ---------------------------
    ## frequencies
    info_freq = models.StringField(
        choices=get_scale_frequency_info(),
        label=_(
            dict(
                en="Over the past 3 months, how often did you acquire information and/or news? For information and news we refer to national, international, and regional/local news, as well as other news facts.",
                fr="Au cours des 3 derniers mois, à quelle fréquence avez-vous consulté des informations et/ou des actualités ? Par informations et actualités, nous entendons les actualités nationales, internationales, régionales/locales, ainsi que d'autres faits d'actualité.", vi="Trong 3 tháng vừa qua, bạn đã tiếp nhận thông tin và/hoặc tin tức với tần suất như thế nào? Ở đây, “thông tin và tin tức” bao gồm tin tức quốc gia, quốc tế, khu vực/địa phương, cũng như các tin tức, sự kiện khác."
            )
        ),
        widget=widgets.RadioSelectHorizontal
    )
    climate_info_freq = models.StringField(
        choices=get_scale_frequency_info(),
        label=_(
            dict(
                en="Over the past 3 months, how often did you acquire information and/or news <b>about climate change</b>? For information and news we refer to national, international, and regional/local news, as well as other news facts.",
                fr="Au cours des 3 derniers mois, à quelle fréquence avez-vous consulté des informations et/ou des actualités <b>sur le changement climatique</b> ? Par informations et actualités, nous entendons les actualités nationales, internationales, régionales/locales, ainsi que d'autres faits d'actualité.", vi="Trong 3 tháng vừa qua, bạn đã tiếp nhận thông tin và/hoặc tin tức <b>về biến đổi khí hậu</b> với tần suất như thế nào? Ở đây, “thông tin và tin tức” bao gồm tin tức quốc gia, quốc tế, khu vực/địa phương, cũng như các tin tức, sự kiện khác."
            )
        ),
        widget=widgets.RadioSelectHorizontal
    )
    ## sources
    use_tv = models.IntegerField(
        label=_(
            dict(
                en="Television (e.g., national news, cable news)",
                fr="Télévision (par exemple, actualités nationales, chaînes d'information)", vi="Truyền hình (ví dụ như tin thời sự quốc gia, tin trên đài truyền hình cáp)"
            )
        ),
        choices=range(1, 8),
        widget=widgets.RadioSelectHorizontal
    )
    use_newspapers = models.IntegerField(
        label=_(
            dict(
                en="Printed Newspapers",
                fr="Journaux imprimés", vi="Báo in"
            )
        ),
        choices=range(1, 8),
        widget=widgets.RadioSelectHorizontal
    )
    use_radio = models.IntegerField(
        label=_(
            dict(
                en="Radio or podcasts",
                fr="Radio ou podcasts", vi="Radio hoặc podcasts"
            )
        ),
        choices=range(1, 8),
        widget=widgets.RadioSelectHorizontal
    )
    use_social = models.IntegerField(
        label=_(
            dict(
                en="Social media platforms",
                fr="Plateformes de médias sociaux", vi="Mạng xã hội"
            )
        ),
        choices=range(1, 8),
        widget=widgets.RadioSelectHorizontal
    )
    use_online = models.IntegerField(
        label=_(
            dict(
                en="News media websites or apps",
                fr="Actualités en ligne", vi="Tin tức trên các trang web truyền thông hoặc các ứng dụng điện thoại"
            )
        ),
        choices=range(1, 8),
        widget=widgets.RadioSelectHorizontal
    )
    use_newsletters = models.IntegerField(
        label=_(
            dict(
                en="Newsletters or email subscriptions",
                fr="Newsletters ou abonnements par e-mail", vi="Bảng tin được gởi qua thư hoặc qua tài khoản mail được đăng ký"
            )
        ),
        choices=range(1, 8),
        widget=widgets.RadioSelectHorizontal
    )
    use_tv_climate = models.IntegerField(
        label=_(
            dict(
                en="Television (e.g., national news, cable news)",
                fr="Télévision (par exemple, actualités nationales, chaînes d'information)", vi="Truyền hình (ví dụ như tin thời sự quốc gia, tin trên đài truyền hình cáp)"
            )
        ),
        choices=range(1, 8),
        widget=widgets.RadioSelectHorizontal
    )
    use_newspapers_climate = models.IntegerField(
        label=_(
            dict(
                en="Printed Newspapers",
                fr="Journaux imprimés", vi="Báo in"
            )
        ),
        choices=range(1, 8),
        widget=widgets.RadioSelectHorizontal
    )
    use_radio_climate = models.IntegerField(
        label=_(
            dict(
                en="Radio or podcasts",
                fr="Radio ou podcasts", vi="Radio hoặc podcasts"
            )
        ),
        choices=range(1, 8),
        widget=widgets.RadioSelectHorizontal
    )
    use_social_climate = models.IntegerField(
        label=_(
            dict(
                en="Social media platforms",
                fr="Plateformes de médias sociaux", vi="Mạng xã hội"
            )
        ),
        choices=range(1, 8),
        widget=widgets.RadioSelectHorizontal
    )
    use_online_climate = models.IntegerField(
        label=_(
            dict(
                en="News media websites or apps",
                fr="Actualités en ligne", vi="Tin tức trên các trang web truyền thông hoặc các ứng dụng điện thoại"
            )
        ),
        choices=range(1, 8),
        widget=widgets.RadioSelectHorizontal
    )
    use_newsletters_climate = models.IntegerField(
        label=_(
            dict(
                en="Newsletters or email subscriptions",
                fr="Newsletters ou abonnements par e-mail", vi="Bảng tin được gởi qua thư hoặc qua tài khoản mail được đăng ký"
            )
        ),
        choices=range(1, 8),
        widget=widgets.RadioSelectHorizontal
    )

#    use_left_sources = models.BooleanField(
#        label=_(
#            dict(
#                en="Left-leaning sources?",
#                fr="Sources orientées à gauche ?"
#            )
#        ),
#        widget=widgets.CheckboxInput, blank=True
#    )
#    use_right_sources = models.BooleanField(
#        label=_(
#            dict(
#                en="Rright-leaning sources?",
#                fr="Sources orientées à droite ?"
#            )
#        ),
#        widget=widgets.CheckboxInput, blank=True
#    )
#    use_neutral_sources = models.BooleanField(
#        label=_(
#            dict(
#                en="Neutral/centrist sources?",
#                fr="Sources neutres/centristes ?"
#            )
#        ),
#        widget=widgets.CheckboxInput, blank=True
#    )
#    unknown_sources_orientation = models.BooleanField(
#        label=_(
#            dict(
#                en="I don’t know the political orientation of my news sources",
#                fr="Je ne connais pas l'orientation politique de mes sources d'information"
#            )
#        ),
#        widget=widgets.CheckboxInput, blank=True
#    )
#    news_preference = models.IntegerField(
#        label=_(
#            dict(
#                en="If given the choice, would you prefer to read news that...",
#                fr="Si vous aviez le choix, préféreriez-vous lire des actualités qui..."
#            )
#        ),
#        choices=[
#            [1, _(dict(en="Confirm your beliefs", fr="Confirment vos croyances"))],
#            [2, _(dict(en="Challenge your beliefs", fr="Remettent en question vos croyances"))],
#            [3,
#             _(dict(en="Provide neutral and factual information",
#                    fr="Fournissent des informations neutres et factuelles"))]
#        ],
#        widget=widgets.RadioSelect
#    )
#    subscribe_newsletter = models.BooleanField(
#        choices=[
#            [True, _(dict(en="Yes", fr="Oui"))],
#            [False, _(dict(en="No", fr="Non"))]
#        ],
#        label=_(
#            dict(
#                en="Would you be willing to subscribe to a newsletter that covers top stories on climate policy "
#                   "from sources across the political spectrum?",
#                fr="Seriez-vous prêt(e) à vous abonner à une newsletter couvrant les princiinpales actualités sur "
#                   "les politiques climatiques provenant de sources de tout le spectre politique ?"
#            )
#        ),
#        widget=widgets.RadioSelectHorizontal
#    )
#    willingness_to_pay = models.IntegerField(
#        label=_(
#            dict(
#                en="How much would you be willing to pay for exclusive, reliable climate news? (one-time payment)",
#                fr="Combien seriez-vous prêt(e) à payer pour des actualités climatiques exclusives et fiables ? "
#                   "(paiement unique)"
#            )
#        ),
#        choices=[
#            [0, _(dict(en=f"{cu(0)}", fr=f"{cu(0)}"))],
#            [1, _(dict(en=f"{cu(0.5)}", fr=f"{cu(0.5)}"))],
#            [2, _(dict(en=f"{cu(1)}", fr=f"{cu(1)}"))],
#            [3, _(dict(en=f"{cu(2)}", fr=f"{cu(2)}"))],
#            [4, _(dict(en=f"More than {cu(2)}", fr=f"Plus de {cu(2)}"))]
#        ],
#        widget=widgets.RadioSelectHorizontal
#    )
    # Concern -------------------------
    climate_threat = models.IntegerField(
        choices=[
            [3, _(dict(en="Very serious threat", fr="Une menace très sérieuse", vi="Mối đe dọa rất nghiêm trọng"))],
            [2, _(dict(en="Somewhat serious threat", fr="Une menace assez sérieuse", vi="Mối đe dọa tương đối nghiêm trọng"))],
            [1, _(dict(en="Not a threat at all", fr="Pas une menace du tout", vi="Hoàn toàn không phải là mối đe dọa"))],
            [0, _(dict(en="Don’t know", fr="Ne sais pas", vi="Không biết"))]
        ],
        label=_(
            dict(
                en="Do you think climate change will be a threat to people in your country in the next 20 years?",
                fr="Pensez-vous que le changement climatique sera une menace pour les gens de votre pays dans les "
                   "20 prochaines années ?", vi="Bạn có nghĩ rằng biến đổi khí hậu sẽ là một mối đe dọa đối với người dân ở Việt Nam trong 20 năm tới không?"
            )
        ),
        widget=widgets.RadioSelectHorizontal
    )
    # Willingness to act --------------
    limit_flying = models.IntegerField(
        label=_(
            dict(
                en="Limit flying",
                fr="Limiter les vols", vi="Hạn chế đi máy bay"
            )
        ),
        choices=get_scale_action(),
        widget=widgets.RadioSelectHorizontal
    )
    limit_driving = models.IntegerField(
        label=_(
            dict(
                en="Limit driving",
                fr="Limiter la conduite", vi="Hạn chế lái xe ô tô"
            )
        ),
        choices=get_scale_action(),
        widget=widgets.RadioSelectHorizontal
    )
    electric_vehicle = models.IntegerField(
        label=_(
            dict(
                en="Have an electric vehicle",
                fr="Posséder un véhicule électrique", vi="Sở hữu một phương tiện chạy điện"
            )
        ),
        choices=get_scale_action(),
        widget=widgets.RadioSelectHorizontal
    )
    limit_beef = models.IntegerField(
        label=_(
            dict(
                en="Limit beef consumption",
                fr="Limiter la consommation de bœuf", vi="Hạn chế tiêu thụ thịt bò"
            )
        ),
        choices=get_scale_action(),
        widget=widgets.RadioSelectHorizontal
    )
    limit_heating = models.IntegerField(
        label=_(
            dict(
                en="Limit heating or cooling your home",
                fr="Limiter le chauffage ou la climatisation de votre maison", vi="Hạn chế sưởi ấm hoặc làm mát nhà của bạn"
            )
        ),
        choices=get_scale_action(),
        widget=widgets.RadioSelectHorizontal
    )
    # Policy support ------------------
    tax_flying = models.StringField(
        label=_(
            dict(
                en="A tax on flying (that increases ticket prices by 20%)",
                fr="Une taxe sur les vols (qui augmente les prix des billets de 20%)", vi="Thuế đối với việc đi máy bay (làm tăng giá vé thêm 20%)"
            )
        ),
        choices=get_scale_policy(),
        widget=widgets.RadioSelectHorizontal
    )
    tax_fossil = models.StringField(
        label=_(
            dict(
                en="A national tax on fossil fuels (increasing gasoline prices by 40 cents per gallon)",
                fr="Une taxe nationale sur les combustibles fossiles (augmentant les prix de l'essence de 40 centimes par gallon)", vi="Thuế quốc gia đối với nhiên liệu hóa thạch (làm tăng giá xăng thêm 40 xu mỗi gallon)"
            )
        ),
        choices=get_scale_policy(),
        widget=widgets.RadioSelectHorizontal
    )
    ban_polluting = models.StringField(
        label=_(
            dict(
                en="A ban of polluting vehicles in dense areas, like city centers",
                fr="Une interdiction des véhicules polluants dans les zones denses, comme les centres-villes", vi="Cấm các phương tiện gây ô nhiễm tại các khu vực đông dân cư, như trung tâm thành phố"
            )
        ),
        choices=get_scale_policy(),
        widget=widgets.RadioSelectHorizontal
    )
    subsidy_lowcarbon = models.StringField(
        label=_(
            dict(
                en="Subsidies for low-carbon technologies (renewable energy, carbon capture...)",
                fr="Des subventions pour les technologies à faible émission de carbone (énergies renouvelables, capture de carbone...)", vi="Trợ cấp cho các công nghệ phát thải thấp (năng lượng tái tạo, thu giữ carbon...)"
            )
        ),
        choices=get_scale_policy(),
        widget=widgets.RadioSelectHorizontal
    )
    climate_fund = models.StringField(
        label=_(
            dict(
                en="A contribution to a global climate fund to finance clean energy in low-income countries",
                fr="Une contribution à un fonds climatique mondial pour financer l'énergie propre dans les pays à faible revenu", vi="Đóng góp vào một quỹ khí hậu toàn cầu để tài trợ năng lượng sạch tại các nước thu nhập thấp"
            )
        ),
        choices=get_scale_policy(),
        widget=widgets.RadioSelectHorizontal
    )
    expectations_droughts = models.StringField(
        label=_(
            dict(
                en="Severe droughts and heatwaves",
                fr="Sécheresses sévères et vagues de chaleur", vi="Hạn hán nghiêm trọng và các đợt nắng nóng kéo dài"
            )
        ),
        choices=get_scale_expectations(),
        widget=widgets.RadioSelectHorizontal
    )
    expectations_eruptions = models.StringField(
        label=_(
            dict(
                en="More frequent volcanic eruptions",
                fr="Éruptions volcaniques plus fréquentes", vi="Có nhiều vụ phun trào núi lửa hơn "
            )
        ),
        choices=get_scale_expectations(),
        widget=widgets.RadioSelectHorizontal
    )
    expectations_sea = models.StringField(
        label=_(
            dict(
                en="Rising sea levels",
                fr="Montée du niveau de la mer", vi="Mực nước biển dâng cao"
            )
        ),
        choices=get_scale_expectations(),
        widget=widgets.RadioSelectHorizontal
    )
    expectations_agriculture = models.StringField(
        label=_(
            dict(
                en="Lower agricultural production",
                fr="Baisse de la production agricole", vi="Sản lượng nông nghiệp thấp hơn"
            )
        ),
        choices=get_scale_expectations(),
        widget=widgets.RadioSelectHorizontal
    )
    expectations_living = models.StringField(
        label=_(
            dict(
                en="Drop in standards of living",
                fr="Baisse du niveau de vie", vi="Chất lượng sống giảm"
            )
        ),
        choices=get_scale_expectations(),
        widget=widgets.RadioSelectHorizontal
    )
    expectations_migration = models.StringField(
        label=_(
            dict(
                en="Larger migration flows",
                fr="Flux migratoires plus importants", vi="Dòng người di cư nhiều hơn"
            )
        ),
        choices=get_scale_expectations(),
        widget=widgets.RadioSelectHorizontal
    )
    expectations_conflicts = models.StringField(
        label=_(
            dict(
                en="More armed conflicts",
                fr="Plus de conflits armés", vi="Các cuộc xung đột vũ trang xuất hiện nhiều hơn"
            )
        ),
        choices=get_scale_expectations(),
        widget=widgets.RadioSelectHorizontal
    )
    expectations_extinction = models.StringField(
        label=_(
            dict(
                en="Extinction of humankind",
                fr="Extinction de l'humanité", vi="Loài người sẽ bị tuyệt chủng"
            )
        ),
        choices=get_scale_expectations(),
        widget=widgets.RadioSelectHorizontal
    )

    # Circadian (anti-bot page)
    circadian = models.StringField(
        label= _(dict(
            en="",
            fr="", vi=""
        ))
    )

    # Demographics
    ## Income
    income = models.IntegerField(
        label= _(dict(
            en="Thinking about your household, what would you estimate is its total net monthly "
               "income on average (after taxes and deductions)? Please include salaries, pensions, family allowances, "
               "unemployment benefits, or any other regular income.",
            fr="En pensant à votre foyer, quel est selon vous son revenu net mensuel total moyen (après impôts et "
               "déductions) ? Veuillez inclure les salaires, retraites, allocations familiales, indemnités de chômage "
               "ou tout autre revenu régulier.", vi="Khi nghĩ về thu nhập của gia đình bố mẹ bạn, bạn ước tính thu nhập ròng trung bình hàng tháng của họ là bao nhiêu (sau khi trừ thuế và các khoản khấu trừ)? Vui lòng bao gồm lương, lương hưu, trợ cấp gia đình, trợ cấp thất nghiệp hoặc bất kỳ nguồn thu nhập định kỳ nào khác."
        )),
        choices=get_scale_income()
    )

    ## Education
    education = models.IntegerField(
        label = _(dict(
          en="What is the highest education level that you have achieved?",
          fr="Quel est le niveau d'études le plus élevé que vous ayez atteint ?", vi="Bạn đã đạt được trình độ học vấn cao nhất là gì?"
        )),
        choices=get_scale_education()
    )

def payoff_mpl(player: Player):
    #players = self.get_players()

    #for p in players:
    if player.is_selected == 1:
        choice_vars = [player.choice_1, player.choice_2, player.choice_3, player.choice_4,
                       player.choice_5, player.choice_6, player.choice_7]
        chosen_choice = choice_vars[player.random_row]

        if chosen_choice == "B":
            player.payoff_mpl = player.random_amount
        else:
            player.payoff_mpl = 0

# ======================================================================================================================
#
# -- PAGES
#
# ======================================================================================================================

class MyPage(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            **language
        )

    @staticmethod
    def js_vars(player: Player):
        return dict(
            fill_auto=player.session.config.get("fill_auto", False),
            **language
        )


class Presentation(MyPage):
    form_model = 'player'
    form_fields = ["skip"]

#    @staticmethod
#    def app_after_this_page(player, upcoming_apps):
#        if player.skip:
#            if player.subsession.prolific:  # If in Prolific mode, end the questionnaire with the End page
#                return None
#            else:
#                return upcoming_apps[-1]  # Skip to the last app (whistleblowing_final
#        else:
#            return None

class NarrativeElicitation_text(MyPage):
    form_model = 'player'

    @staticmethod
    def is_displayed(player: Player):
        return player.skip == False

class NarrativeElicitation_question(MyPage):
    form_model = 'player'
    form_fields = ['climate_exists', 'narrative_elicitation']

    @staticmethod
    def is_displayed(player: Player):
        return player.skip == False

    @staticmethod
    def error_message(player, values):
        text = values['narrative_elicitation'] or ""
        word_count = len(text.split())

        if word_count < 50:
            return _(dict(
                en=f"Please write at least 50 words (you wrote {word_count}).",
                fr=f"Veuillez écrire au moins 50 mots (vous en avez écrit {word_count}).", vi=f"Vui lòng viết ít nhất 50 từ (bạn đã viết {word_count} từ)."
            ))
#        if len(values['narrative_elicitation']) < 50:
#            return "Please write at least 50 characters."


class NarrativeElicitation_question_certain(MyPage):
    form_model = 'player'
    form_fields = ['narrative_confidence']

    @staticmethod
    def is_displayed(player: Player):
        return player.skip == False

class NarrativeSharing(MyPage):
    form_model = 'player'
    form_fields = [
                   'choice_1', 'choice_2', 'choice_3',
                   'choice_4', 'choice_5', 'choice_6', 'choice_7'
                   ]

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        payoff_mpl(player)

    @staticmethod
    def is_displayed(player: Player):
        return player.skip == False

class circadian(MyPage):
    form_model = 'player'
    form_fields = ['circadian']

    @staticmethod
    def is_displayed(player: Player):
        return player.skip == False

class Policy(MyPage):
    form_model = 'player'
    form_fields = ['policy_fight', 'policy_narrative']

    @staticmethod
    def is_displayed(player: Player):
        return player.skip == False

    @staticmethod
    def error_message(player, values):
        #if len(values['policy_narrative']) < 50:
        #    return "Please write at least  characters."
        text = values['policy_narrative'] or ""
        word_count = len(text.split())

        if word_count < 25:
            return _(dict(
                en=f"Please write at least 25 words (you wrote {word_count}).",
                fr=f"Veuillez écrire au moins 25 mots (vous en avez écrit {word_count}).", vi=f"Vui lòng viết ít nhất 25 từ (bạn đã viết {word_count} từ)."
            ))

class Policy_question_certain(MyPage):
    form_model = 'player'
    form_fields = ['confidence_policy']

    @staticmethod
    def is_displayed(player: Player):
        return player.skip == False

class Policy_expectations(MyPage):
    form_model = 'player'
    form_fields = ['expectations_policy_economy', 'expectations_policy_cc', 'expectations_policy_household',
                   'agreement_policy']

    @staticmethod
    def is_displayed(player: Player):
        return player.skip == False

class ClimateKnowledge(MyPage):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player):
        fields = ["climate_knowledge"]
        ranks = ["rank_coal", "rank_gas", "rank_nuclear"]
        random.shuffle(ranks)
        fields += ranks
        return fields

    # def error_message(self, values):
    #     ranks = [values['rank_coal'], values['rank_gas'], values['rank_nuclear']]
    #     if sorted(ranks) != [1, 2, 3]:
    #         return _(dict(
    #             en="Please assign a unique rank (1, 2, and 3) to each energy source.",
    #             fr="Veuillez assigner un classement unique (1, 2 ou 3) à chaque source d'énergie."
    #         ))
    #     return None

    @staticmethod
    def is_displayed(player: Player):
        return player.skip == False


class MediaConsumption(MyPage):
    form_model = 'player'
    form_fields = ['info_freq',
        'use_tv', 'use_newspapers', 'use_radio', 'use_social', 'use_online', 'use_newsletters',
        'climate_info_freq',
        'use_tv_climate', 'use_newspapers_climate', 'use_radio_climate', 'use_social_climate', 'use_online_climate', 'use_newsletters_climate',
    ]

    @staticmethod
    def is_displayed(player: Player):
        return player.skip == False


class ClimateExpectations(MyPage):
    form_model = 'player'
    form_fields = [
        'climate_threat',
        'expectations_droughts', 'expectations_eruptions', 'expectations_sea', 'expectations_agriculture', 'expectations_living', 'expectations_migration', 'expectations_conflicts', 'expectations_extinction'
    ]

    @staticmethod
    def vars_for_template(player: Player):
        existing = MyPage.vars_for_template(player)
        existing["scale_expectations"] = [s[1] for s in get_scale_expectations()]
        return existing

    @staticmethod
    def is_displayed(player: Player):
        return player.skip == False

class ClimateConcern(MyPage):
    form_model = 'player'
    form_fields = [
        'limit_flying', 'limit_driving', 'electric_vehicle', 'limit_beef', 'limit_heating'
    ]

    @staticmethod
    def vars_for_template(player: Player):
        existing = MyPage.vars_for_template(player)
        existing["scale_policy"] = [s[1] for s in get_scale_policy()]
        return existing


    @staticmethod
    def is_displayed(player: Player):
        return player.skip == False

class Prolific_Page(MyPage):

    @staticmethod
    def vars_for_template(player: Player):
        existing = MyPage.vars_for_template(player)
        existing["link"] = player.session.config['prolific_link']
        return existing
    pass

class Demographics(MyPage):
    form_model = 'player'
    form_fields = ['income', 'education']

    @staticmethod
    def is_displayed(player: Player):
        return player.skip == False

class End(MyPage):
    @staticmethod
    def vars_for_template(player: Player):
        existing = MyPage.vars_for_template(player)
        existing.update(
            url_validate=player.session.config.get("url_validate", ""),
            url_return=player.session.config.get("url_return", "")
        )
        return existing


page_sequence = [Presentation,
                 NarrativeElicitation_text, NarrativeElicitation_question, NarrativeElicitation_question_certain, circadian, NarrativeSharing,
                 Policy, Policy_question_certain, Policy_expectations,
                 ClimateKnowledge, MediaConsumption,
                 ClimateExpectations,
                 ClimateConcern,
                 Demographics,
                 End]