def print_report(fields: dict) -> None:
    print("=== REPORT ===")
    for key, value in fields.items():
        print(f"{key}: {value}")
    print("==============")


def create_user_report(user: dict) -> None:
    print_report({"Name": user["name"], "Email": user["email"]})


def create_order_report(order: dict) -> None:
    print_report({"ID": order["id"], "Total": order["total"]})


def create_payment_report(payment: dict) -> None:
    print_report({"Amount": payment["amount"], "Status": payment["status"]})

create_user_report({"name": "Denis", "email": "denis@test.com"})
create_order_report({"id": 1, "total": 250.0})
create_payment_report({"amount": 100.0, "status": "completed"})
