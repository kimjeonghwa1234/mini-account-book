from utils.storage import load_records, save_records

def show_menu():
    print("\n==== 미니 가계부 ====")
    print("1. 수입/지출 추가")
    print("2. 전체 내역 보기")
    print("3. 키워드로 검색")
    print("4. 잔액 확인")
    print("5. 종료")
    print("=====================")

def add_record(records):
    record_type = input("타입 선택 (수입/지출): ")
    if record_type not in ["수입", "지출"]:
        print("잘못된 입력입니다.")
        return

    try:
        amount = int(input("금액: "))
    except:
        print("금액은 숫자만 입력하세요.")
        return

    desc = input("설명: ")

    record = {
        "type": record_type,
        "amount": amount,
        "desc": desc
    }
    records.append(record)
    save_records(records)
    print("등록 완료!")

def show_all(records):
    print("\n=== 전체 내역 ===")
    if not records:
        print("내역이 없습니다.")
    for idx, r in enumerate(records, 1):
        print(f"{idx}. [{r['type']}] {r['amount']}원 - {r['desc']}")
    print("================")

def search_record(records):
    keyword = input("검색 키워드: ")
    print(f"\n=== '{keyword}' 검색 결과 ===")
    found = False
    for r in records:
        if keyword in r['desc']:
            print(f"[{r['type']}] {r['amount']}원 - {r['desc']}")
            found = True
    if not found:
        print("검색 결과가 없습니다.")

def show_balance(records):
    income = sum(r['amount'] for r in records if r['type'] == "수입")
    spend = sum(r['amount'] for r in records if r['type'] == "지출")
    print(f"\n총 잔액: {income - spend}원")

def main():
    records = load_records()

    while True:
        show_menu()
        choice = input("선택: ")

        if choice == "1":
            add_record(records)
        elif choice == "2":
            show_all(records)
        elif choice == "3":
            search_record(records)
        elif choice == "4":
            show_balance(records)
        elif choice == "5":
            print("종료합니다.")
            break
        else:
            print("잘못된 입력입니다.")

if __name__ == "__main__":
    main()
