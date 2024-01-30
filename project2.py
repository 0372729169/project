def message(name,number):
    if int(number)==1:
        print(f'{name} رو به اتمام موجودی است')
    if int(number)==0:
        print(f' موجودی {name} به پایان رسیده است')
def add_prodect(d,l1):
    d[l1[0]]=l1[1:]
    print(f'{l1[0]}به محصولات فروشگاه اضافه شد ')
def generate_invoice(dic,factor):
    if factor in dic.keys():
        for i in range(0,len(dic[factor]),2):
            print(f'نام محصول:{dic[factor][i]}و تعداد سفارش:{dic[factor][i+1]}و قیمت نهایی:{int(d[dic[factor][i]][0])*int(dic[factor][i+1])}')
    else:
        print('فاکتور مورد نظر موجود نمی باشد')
def generate_report(d,dic,nam):
    price=int(dic[nam])*int(d[nam][0])
    print(f'این محصول تاکنون به تعداد {dic[nam]} با قیمت نهایی {d[nam][0]} سفارش داده شده است')
n=int(input('{لطفا برای جدا کردن موارد خواسته شده از علامت منها استفاده نمایید}تعداد محصولات فروشگاه را وارد نمایید:'))
d={}
num_order=0
mony=0
d_number={}
for i in range(n):
    l=list(input('لطفا به ترتیب نام کالا و قیمت و موجودی و توضیحات را وارد نمایید:').split('-'))
    d_number[l[0]]=0
    d[l[0]]=l[1:]
for j in range(10**100):
    a=int(input('شماره عملیات مورد نظر را وارد کنید(1-افزودن کالا 2-مدیریت موجودی 3-پردازش سفارشات 4-دریافت فاکتور محصول 5-دریافت گزارش 6-پایان )):'))
    if a==1:
        l1=list(input('لطفا به ترتیب نام کالا و قیمت و موجودی و توضیحات را وارد نمایید:').split('-'))
        add_prodect(d,l1)
        print(f'لیست محصولات موجود:{d}')
    elif a==2:
         b=int(input('شماره عملیات مورد نظر را وارد کنید(1-تغییر موجودی کالاها 2-دریافت لیست موجودی فعلی کالاها ):'))
         if b==1:
             c=int(input('تعداد کالاهایی که نیاز به تغییر موجودی دارند را وارد کنید:'))
             for r in range(c):
                 name,number=input('نام کالای مورد نظر و موجودی جدید را وارد کنید: ').split('-')
                 d[name]=number
                 print(f' موجودی {name} به {number}تغییر کرد')
                 print(f'لیست محصولات موجود:{d}')
                 message(name,number)
         elif b==2:
             d1={}
             for s in d.keys():
                 d1[s]=d[s][1]
             print(d1)
             for t in d1.keys():
                 message(t,d1[t])
    elif a==3:
        nu_order=input('تعداد کالای سفارش داده شده را وارد کنید:')
        num_order+=int(nu_order)
        factor=input('شماره فاکتور را وارد نمایید:')
        d2={}
        for h in range(int(nu_order)):
            na,nu=input('نام کالای سفارش داده شد و تعداد را وارد کنید: ').split('-')
            d2[factor]=[]
            d2[factor].append(na)
            d2[factor].append(nu)
            item=int(d_number[na])+int(nu)
            d_number[na]=item
            if int(d[na][1])>=int(nu):
                s=int(d[na][1])-int(nu)
                d[na][1]=s
                mony+=(int(d[na][0])*int(nu))
                print(f' موجودی {na} به {s} تغییر پیدا کرد' )
                print(f'لیست محصولات موجود:{d}')
                message(na,s)
            else:
                print(f'موجودی {na} برای سفارش مورد نظر کافی نیست')
    elif a==4:
        factor_nu=input('شماره فاکتور را وارد نمایید:')
        generate_invoice(d2,factor_nu)
    elif a==5:
        re=int(input('شماره عملیات مورد نظر را وارد کنید:1-دریافت گزارش تعداد سفارشات 2-دریافت گزارش تعداد سفارش از یک محصول:'))
        if re==1:
            print(f'تاکنون به تعداد {num_order} سفارش از فروشگاه به مبلغ نهایی {mony} انجام شده است')
            print(f'لیست محصولات موجود:{d}')
        if re==2:
            nam=input('نام کالای مورد نظر را وارد نمایید:')
            generate_report(d,d_number,nam)
            print(f'لیست محصولات موجود:{d}')
    elif a==6:
        print("مدیریت فروشگاه پایان یافت. خدانگهدار")
        break