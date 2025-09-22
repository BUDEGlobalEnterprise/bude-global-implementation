# 🚀 The Ultimate Community ERPNext Master Setup Checklist ✅

This checklist is designed to be a comprehensive guide for anyone implementing ERPNext, from a small business to a large organization. It follows a logical implementation sequence.

---

## 📋 Phase 0: Pre-Implementation Planning

*   [ ] **Define Project Goals & Scope:** What problems are we solving?
*   [ ] **Form an Implementation Team:** Identify key users and a project lead.
*   [ ] **Plan Your Data Migration Strategy:** How will you bring existing data in?
*   [ ] **Set Up a Testing Instance:** Never configure directly on production!
*   [ ] **Schedule User Training Sessions:** Plan for early and often training.

---

## 🔧 Phase 1: The Foundation - System & Company Setup

*   [ ] **Create System Users** (for team members)
*   [x] **Create Your First Company**
    *   [x] Company Name & Abbreviation
    *   [x] Default Currency & Chart of Accounts
    *   [ ] Default Letterhead (with logo and address)
    *   [ ] Fiscal Year Definition
*   [x] **Configure Global Defaults**
    *   [x] Country, Timezone, Date/Number Format

---

## 👥 Phase 2: People & Structure - HR Masters

*   [x] **Departments** (e.g., Sales, Accounting, Production)
*   [x] **Designations** (e.g., Manager, Executive, Analyst)
*   [ ] **Employee Grades** (e.g., A, B, C or Junior, Senior)
*   [x] **Branch** (if applicable, e.g., Head Office, Branch 1)
*   [ ] **Create Employee Records** (for all users)
*   [x] **Holiday List** (Upload your country's holiday calendar)
*   [x] **Leave Types** (e.g., Annual Leave, Sick Leave, Casual Leave)
*   [ ] **Leave Policy** (Rules for allocating leave)

---

## 📦 Phase 3: What You Sell & Buy - Item & Inventory Masters

*   [ ] **Item Groups** (e.g., `Products -> Electronics -> Phones`, `Services -> Consulting`)
*   [ ] **Units of Measure (UOM)** (e.g., Nos, Kg, Meter, Hour, Packet, Box)
*   [ ] **Warehouses** (e.g., `Stores`, `Finished Goods`, `Work-in-Progress`, `Damage`)
*   [ ] **Items** (Your products and services)
    *   [ ] Item Code & Name
    *   [ ] Assign to an Item Group
    *   [ ] Define UOM
    *   [ ] Set standard Selling & Buying Rates
    *   [ ] Apply HSN/SAC Code for taxes (if applicable)

---

## 🤝 Phase 4: Who You Work With - Customer & Supplier Masters

*   [ ] **Customer Groups** (e.g., `Individual`, `Commercial`, `Government`, `Online`)
*   [ ] **Supplier Groups** (e.g., `Raw Material`, `Services`, `Local`, `International`)
*   [ ] **Territory** (e.g., `Domestic`, `North America`, `Europe`, `Asia`)
*   [ ] **Sales Persons** (Assign your team members)
*   [ ] **Add Individual Customer Records**
*   [ ] **Add Individual Supplier Records**

---

## 💰 Phase 5: Money & Accounts - Finance Masters

*   [ ] **Mode of Payment** (e.g., `Cash`, `Bank Transfer`, `Credit Card`, `Cheque`)
*   [ ] **Bank Account** (Add your company's bank accounts)
*   [ ] **Cost Centers** (e.g., `Sales`, `Marketing`, `Administration`) - **Crucial for reporting!**
*   [ ] **Taxes** (Setup your tax templates, e.g., `GST 18%`, `VAT 5%`, `Sales Tax`)
*   [ ] **Price Lists** (e.g., `Standard Selling`, `Standard Buying`, `Wholesale`)

---

## ⚙️ Phase 6: Operations & Workflows (Optional)

*   [ ] **Manufacturing**
    *   [ ] Operations (steps in production, e.g., `Cutting`, `Assembly`)
    *   [ ] Workstations (machines or locations for operations)
    *   [ ] Bill of Materials (BOM - recipe for finished goods)
*   [ ] **Projects**
    *   [ ] Project Types (e.g., `Internal`, `Customer`)
*   [ ] **Assets**
    *   [ ] Asset Categories (e.g., `Computers`, `Machinery`, `Furniture`)

---

## ✉️ Phase 7: Communication & Automation

*   [ ] **Email Account** (Setup incoming email for support tickets, etc.)
*   [ ] **Email Templates** (for Quotations, Invoices, Support replies)
*   [ ] **Print Headings & Terms** (Standard T&C for quotes and invoices)
*   [ ] **Print Formats** (Customize how PDFs look)
*   [ ] **Notification Settings** (What alerts should users get?)

---

## 🔐 Phase 8: Security & Roles - User Access Control

*   [ ] **Define User Roles** (e.g., `Accounts User`, `Sales Manager`, `Stock Manager`)
*   [ ] **Set Role Permissions** (Who can see, create, edit, delete, submit, cancel)
*   [ ] **Assign Roles to Users** (Give people the access they need, nothing more)

---

## 📊 Phase 9: Reporting & Go-Live

*   [ ] **Test Key Reports:** Profit and Loss, Balance Sheet, Stock Summary, Sales Analytics
*   [ ] **Enter Opening Balances** (for Accounts, Inventory, Debtors, Creditors)
*   [ ] **Final Data Migration Check**
*   [ ] **Confirm User Training is Complete**
*   [ ] **Announce Go-Live Date! 🎉**

---

## 🧪 **Testing Scenarios (Do This Before Go-Live!)**

**Test a Sales Cycle:**
1.  [ ] Create a **Quotation** for a Customer
2.  [ ] Convert it to a **Sales Order**
3.  [ ] Create a **Delivery Note** (update stock)
4.  [ ] Create a **Sales Invoice** (update accounting)
5.  [ ] Receive a **Payment** against the invoice

**Test a Purchase Cycle:**
1.  [ ] Create a **Purchase Order** for a Supplier
2.  [ ] Create a **Purchase Receipt** (update stock)
3.  [ ] Create a **Purchase Invoice** (update accounting)
4.  [ ] Make a **Payment** to the supplier

---

### 🤝 **Community Contribution Note**
*   **This is a living document.** Feel free to copy, share, and modify it for your needs.
*   **Found something missing?** Add it to your copy!
*   **Share your learnings** with the community forums to help others.

**Happy Implementing!** The ERPNext community is here to help. 🚀