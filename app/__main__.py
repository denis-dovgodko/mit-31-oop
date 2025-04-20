from models.entities import *
from models.repositories import *
from services import PaymentSystem

if __name__ == "__main__":
    owner1 = Owner("Alice", 325790724, True)
    owner2 = Owner("Bob", 957358374, False)
    owner3 = Owner("Charlie", 415357805, True)

    owner2.tax_id = 342

    company1 = Company("Intellias", 10000)
    company2 = Company("Test", 10000)
    company1.add_entity(owner1.name, 5000)
    company1.add_entity(owner2.name, 3000)
    company1.set_annual_profit(2025, 84345)
    company2.add_entity(owner1.name, 3000)
    company2.add_entity(owner3.name, 3000)

    print(yaml_repository.find(OwnerList.path, "name", "Alice").get("is_resident"))

    PaymentSystem.calculate_taxes(company1, 2025)

    # PaymentSystem.calculate_taxes(owner1, 2025)
    # PaymentSystem.calculate_taxes(owner2, 2025)
    
    print(PaymentSystem.performed_payments)
    print(PaymentSystem.total_payed_taxes)
