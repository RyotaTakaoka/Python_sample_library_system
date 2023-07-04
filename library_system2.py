search_title = 0
lental = 0
return_title = 0
return_answer = 0
search_answer = 0
search_answer2 = 0

library_stock = {"むくの冒険":"貸出可",
                 "むっくるの経済学講義":"貸出中",
                 "ゴジラ対サウルス":"貸出可",
                 "タイガとタイピの最上お肉グルメ":"貸出可",
                 "ヒメグマの最強経営術":"貸出中"}

print("図書館貸し出し管理システムです")
print("検索したい本のタイトルを入力してください")
print("借りた本を返却する場合は半角で「1」を入力してください")
print("検索を中断する場合は半角で「99」を入力してください")

while search_title != "99":
    search_title = input("本のタイトルもしくは数字を入力>>")
    
    if search_title == "99":
        print("検索サービスを終了します")
        break
    elif search_title == "1":
        return_title = input("返却する本のタイトルを入力>>")
        return_answer = (return_title, "貸出中") in library_stock.items()
        if return_answer == False:
            print("この本は貸し出されていません")
            continue
        elif return_answer == True:
            del library_stock[return_title]
            library_stock[return_title] = "貸出可"
            print("{}を返却しました".format(return_title))
            print("{}を貸出可に変更しました".format(return_title))
            continue
    else:
        pass
    search_answer = search_title in library_stock.keys()
    if search_answer == True:
        search_answer2 = (search_title, "貸出可") in library_stock.items()
        if search_answer2 == True:
            print("お探しの本は貸し出しが可能です")
            print("この本を借りますか？")
            while lental!= 1 or lental != 0:
                print("借りる場合は「１」を、借りない場合は「０」を入力")
                lental = int(input("「１」か「０」を「半角で入力>>"))
                if lental == 1:
                    del library_stock[search_title]
                    library_stock[search_title] = "貸出中"
                    print("{}を貸出中に変更しました".format(search_title))
                    lental = 0
                    break
                elif lental == 0:
                    print("引き続き検索システムをご利用ください")
                    break
                else:
                    print("指定された番号を入力してください")
                    lental = 0
                
        elif search_answer2 == False:
            print("お探しの本はほかの利用者に貸し出し中です")
            continue
        else:
            pass
    else:
        print("お探しの本は本館にはございません")
