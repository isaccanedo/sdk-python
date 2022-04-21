from .nonBoletoPayment import generateExampleNonBoletoPaymentsJson


def generateExampleUtilityPaymentsJson(n=1, amount=None, next_day=False):
    return generateExampleNonBoletoPaymentsJson(
        n=n,
        amount=amount,
        next_day=next_day,
        is_tax=False,
    )
