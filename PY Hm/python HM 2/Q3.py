import random


def poker_game():
    """
    :rtype: List[List[str]]
    """

    # 红桃, 黑桃, 梅花, 方块
    suit = ['H', 'S', 'C', 'D']
    nums = [str(i) for i in range(1, 11)] + ['J', 'Q', 'K']

    # 请补全代码，生成所有的扑克牌，形如[H1, H2, ..., HK, S1, S2, ..., DK]
    all_cards = []
    for x in suit:
        for y in nums:
            all_cards += [x + y]

    # 加入大小王
    all_cards += ['RJ', "BJ"]

    # 请补全洗牌代码
    wash_cards = []
    for i in range(54):
        wash_cards.append(random.choice(all_cards))
        all_cards.remove(wash_cards[i])

    # 请自行设计发牌规则，为3个玩家发牌。
    player1_cards = []
    player2_cards = []
    player3_cards = []

    # 请补全发牌代码
    for x in range(54):
        if x%3 == 0:
            player1_cards.append(wash_cards[x])
        elif x%3 == 1:
            player2_cards.append(wash_cards[x])
        else:
            player3_cards.append(wash_cards[x])

    # 请补全代码，对玩家手牌排序

    player1_cards.sort()
    player3_cards.sort()
    player2_cards.sort()

    # 最终结果保存在results中，其中每个list保存一个玩家的扑克牌
    results = [player1_cards, player2_cards, player3_cards]

    return results


print(poker_game())
