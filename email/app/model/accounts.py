from webapp.account.models import Account


def find_account(email):

    """
    Finds and returns the account with the
    given email address. Returns None
    if nothing is found.
    """

    try:
        return Account.objects.get(pk=email)
    except Account.DoesNotExist:
        return None
    

def create_account(email):
    
    """
    Returns an account if it already
    exists, otherwise creates it.
    """

    acc = find_account(email)
    if not acc:
        acc = Account(email=email)
        acc.save()
    return acc

