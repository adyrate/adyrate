from django.shortcuts import render, redirect, get_object_or_404

from .models import *
from shops.models import *
from events.models import *
from accounts.models import *
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from random import *



def index(request):


    # searching from homepage ------------------------------------

    query = request.POST.get('search_query')

    query = str(query).lower()


    store = StoreProfile.objects.all()

    if query != None:
        for i in store:
            if query == str(i.store).lower():
                link = "http://localhost:8000/adyrate.com/" + str(i.store).lower()
                return redirect(link)


    # ------------------------------------------------------------

    return render(request, 'index.html', {})


def get_store_id(store_name):

    all_stores = StoreProfile.objects.all()
    found = False
    for i in all_stores:
        if store_name == str(i).lower():
            found = True
            return i.id

    if found == False:
        return None



def submit_review(request, store_instance):


    if request.method == 'POST':

        rate1 = request.POST.get('rating1')
        rate2 = request.POST.get('rating2')
        rate3 = request.POST.get('rating3')
        rate4 = request.POST.get('rating4')
        rate5 = request.POST.get('rating5')
        comment = request.POST.get('comment')



    # -----------------------------------   PROCESS : (1) : if user is loggedIn    ---------------------------

        if request.user.is_authenticated():

            user_id = request.user.id
            user_instance = User.objects.get(id=user_id)


            review = Reviews(client = store_instance.store,
                             user = user_instance,
                             rating = rate1,
                             food_quality = rate2,
                             value_for_money = rate3,
                             hygiene = rate4,
                             service = rate5,
                             comment = comment,
                             )

            review.save()                                           # 1. Review submitted

            store_instance.ady_points_given += store_instance.ady_points
            store_instance.save()
            print ("store given points updated")                      # 2. Store's given points Updated



            try:
                wallet_instance = UserWallet.objects.get(id = user_id)
                wallet_instance.wallet_balance += store_instance.ady_points
                wallet_instance.save()


            except UserWallet.DoesNotExist:
                new_user = UserWallet(user = user_instance, wallet_balance = store_instance.ady_points)
                new_user.save()
                print("New User Created with a wallet balance")



            credit_instance = CreditTransaction(user = user_instance,
                                                client = store_instance.store,
                                                credited_ady_points = store_instance.ady_points,
                                                )
            credit_instance.save()


            return True




    # -----------------------------------   PROCESS : (2) : if user is NOT loggedIn    ---------------------------


        else:

            cookie = randrange(58687, 5868700)

            temp_review = TempReviews(client = store_instance.store,
                                      cookie = cookie,
                                      rating = rate1,
                                      food_quality = rate2,
                                      value_for_money = rate3,
                                      hygiene = rate4,
                                      service = rate5,
                                      comment = comment,
                                      )
            temp_review.save()


            return cookie



def store(request, store_name=None):
    store_id = get_store_id(store_name)
    store_instance = get_object_or_404(StoreProfile, id=store_id)



    status = submit_review(request, store_instance)

    if status == True:
        return redirect('profile_page')
    elif type(status) == type(0):
        cookie = status
        link = 'http://localhost:8000/adyrate.com/accounts/login/'
        response = redirect(link)
        response.set_cookie('unregistered_user_id', cookie)
        return response


    # data for Store_profile
    total_reviews = 0
    avg_rating = 0
    quality = 0
    value_for_money = 0
    hygiene = 0
    service = 0


    reviews = Reviews.objects.filter(client = store_instance.store)
    for i in reviews:
        avg_rating += i.rating
        quality += i.food_quality
        value_for_money += i.value_for_money
        hygiene += i.hygiene
        service += i.service



    total_reviews = float(len(reviews))

    if int(len(reviews)) == 0:
        pass
    else:
        avg_rating = round((avg_rating/total_reviews),2)
        quality = round((quality/total_reviews),2)
        value_for_money = round((value_for_money/total_reviews),2)
        hygiene = round((hygiene/total_reviews),2)
        service = round((service/total_reviews),2)

        total_reviews = int(total_reviews)



#   rating brekdown

    rating1 = Reviews.objects.filter(client = store_instance.store).filter(rating = 1)
    rating2 = Reviews.objects.filter(client=store_instance.store).filter(rating=2)
    rating3 = Reviews.objects.filter(client=store_instance.store).filter(rating=3)
    rating4 = Reviews.objects.filter(client=store_instance.store).filter(rating=4)
    rating5 = Reviews.objects.filter(client=store_instance.store).filter(rating=5)

    discounts = Discounts.objects.filter(store = store_instance.store).filter(status = True)



    context = {
        'store_instance': store_instance,
        'discounts' : discounts,
        'avg_rating' : avg_rating,
        'quality' : quality,
        'value_for_money' : value_for_money,
        'hygiene' : hygiene,
        'service' : service,
        'total_reviews': total_reviews,
        'rating1' : rating1,
        'rating2' : rating2,
        'rating3' : rating3,
        'rating4' : rating4,
        'rating5' : rating5,
        'reviews' : reviews,
    }


    return render(request, 'store.html', context)


def profile(request):

    user_id = request.user.id
    user_instance = User.objects.get(id = user_id)

    user_wallet = UserWallet.objects.get(user = user_instance)
    balance = user_wallet.wallet_balance

    context = {
        'balance' : balance,
    }


    if 'unregistered_user_id' in request.COOKIES:
        cookie = request.COOKIES['unregistered_user_id']

        temp_review = TempReviews.objects.get(cookie = cookie)

        client_instance = temp_review.client
        store_instance = StoreProfile.objects.get(store = client_instance)


        review = Reviews(client = store_instance.store,
                         user = user_instance,
                         rating = temp_review.rating,
                         food_quality = temp_review.food_quality,
                         value_for_money = temp_review.value_for_money,
                         hygiene = temp_review.hygiene,
                         service = temp_review.service,
                         comment = temp_review.comment,
                         )

        review.save()                                           # 1. Review submitted

        store_instance.ady_points_given += store_instance.ady_points
        store_instance.save()
        print ("store given points updated")                      # 2. Store's given points Updated

        try:
            wallet_instance = UserWallet.objects.get(id = user_id)
            wallet_instance.wallet_balance += store_instance.ady_points
            wallet_instance.save()


        except UserWallet.DoesNotExist:
            new_user = UserWallet(user = user_instance, wallet_balance = store_instance.ady_points)
            new_user.save()
            print("New User Created with a wallet balance")         # 3. Userwallet Updated



        credit_instance = CreditTransaction(user = user_instance,
                                            client = store_instance.store,
                                            credited_ady_points = store_instance.ady_points,
                                            )
        credit_instance.save()                                  # 4. credit transaction Updated


        temp_review.delete()

        response = render(request, 'profile.html')
        response.delete_cookie('unregistered_user_id')
        return response

    return render(request, 'profile.html', context)


def coupons(request):

    if request.user.is_authenticated:


        if request.method  == 'POST':


            user_id = request.user.id
            user_instance = User.objects.get(id=user_id)

            selected_discount_id = request.POST.get('selected_coupon')                # type -> str
            selected_discount_id = int(selected_discount_id)

            selected_discount = Discounts.objects.get(id = selected_discount_id)

            store_id = selected_discount.store
            store_instance = StoreProfile.objects.get(store = store_id)

            user_wallet = UserWallet.objects.get(user = user_instance)

            if user_wallet.wallet_balance >= selected_discount.ady_points:

                new_coupon = Coupons(user = user_instance,
                                     store = store_instance.store,
                                     ady_points_cost = selected_discount.ady_points,
                                     discount_percentage = selected_discount.discount_percentage,
                                     status = False
                                     )
                new_coupon.save()

                user_wallet.wallet_balance -= selected_discount.ady_points
                user_wallet.save()

                store_instance.ady_points_given += selected_discount.ady_points
                store_instance.save()

                return redirect('wallet_page')
            else:
                return HttpResponse("you have insufficient Balance")


    else:
        return redirect('account_login')

    return HttpResponse("done!!1")


def testing(request):


    return render(request, 'testing.html', {})


def redeem(request, coupon_id = None):                  # type coupon_id -> str

    coupon_id = int(coupon_id)
    coupon_instance = Coupons.objects.get(id = coupon_id)

    client_instance = coupon_instance.store
    store_instance = StoreProfile.objects.get(store = client_instance)

    user_id = request.user.id
    user_instance = User.objects.get(id = user_id)

    context = {
        'store_instance' :store_instance,
        'coupon_instance' : coupon_instance,


    }
    if request.method == 'POST':

        redeem_amount = request.POST.get('redeem_amount')
        redeem_amount = float(redeem_amount)
        print("Redeem: ", redeem_amount)

        discount_percentage = coupon_instance.discount_percentage
        discount_percentage = float(discount_percentage)

        discount = (redeem_amount*discount_percentage)/100.00

        new_bill = redeem_amount - discount

        # print("Redeem Amount: ", redeem_amount)
        # print("Discount: ", discount)
        # print("new_bill", new_bill)

        redeem_tansaction = RedeemTransaction(user = user_instance,
                                              store = store_instance.store,
                                              discount_percentage = discount_percentage,
                                              before_discount = redeem_amount,
                                              discount = discount,
                                              after_discount = new_bill,
                                              )
        redeem_tansaction.save()

        coupon_instance.status = True
        coupon_instance.save()

        store_instance.ady_points_redeemed += coupon_instance.ady_points_cost
        store_instance.save()

        context['new_bill'] = new_bill
        context['discount'] = discount
        context['old bill'] = redeem_amount

        return  render(request, 'testing.html', context)






    return render(request, 'redeem.html', context)



def wallet(request):


    if request.user.is_authenticated():
        user_id = request.user.id
        user_instance = User.objects.get(id=user_id)

        user_wallet = UserWallet.objects.get(id= user_id)

        coupons_list = Coupons.objects.filter(user = user_instance).filter(status = False)






        context = {
            'user_balance' : user_wallet.wallet_balance,
            'coupons_list' : coupons_list,
        }


        return render(request, 'wallet.html', context)

    return redirect('account_login')


