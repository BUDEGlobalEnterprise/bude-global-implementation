Of course! Here is the Appraisal Template in a clean CSV format, ready for import into ERPNext.

### **Step 1: Save the KRAs (Key Result Areas) as a CSV file**

**File Name:** `appraisal_kras.csv`

```csv
id,kra,per_weightage
KRA-1,Technical Competence & Code Quality,30
KRA-2,Project Delivery & Productivity,25
KRA-3,Teamwork & Collaboration,20
KRA-4,Problem-Solving & Innovation,15
KRA-5,Professional Development & Initiative,10
```

### **Step 2: Save the Rating Criteria as a CSV file**

**File Name:** `appraisal_criteria.csv`

```csv
id,parent,criteria,rating,per_weightage
1.1,KRA-1,Demonstrates strong proficiency in required programming languages and frameworks.,1-5,7.5
1.2,KRA-1,Produces clean, well-documented, and maintainable code. Adheres to best practices.,1-5,7.5
1.3,KRA-1,Effectively uses version control (Git) and conducts thorough code reviews.,1-5,7.5
1.4,KRA-1,Code is robust with minimal bugs. Writes effective unit/integration tests.,1-5,7.5
2.1,KRA-2,Consistently meets project deadlines and delivers tasks on schedule.,1-5,10
2.2,KRA-2,Accurately estimates task complexity and effort required.,1-5,7.5
2.3,KRA-2,Maintains high productivity and manages workload effectively.,1-5,7.5
3.1,KRA-3,Communicates clearly and effectively with team members and stakeholders.,1-5,5
3.2,KRA-3,Actively collaborates, shares knowledge, and supports other team members.,1-5,7.5
3.3,KRA-3,Adapts to team processes and contributes to a positive team environment.,1-5,7.5
4.1,KRA-4,Demonstrates strong analytical skills and effectively troubleshoots complex issues.,1-5,7.5
4.2,KRA-4,Proposes innovative solutions and improvements to systems and processes.,1-5,7.5
5.1,KRA-5,Proactively takes on new challenges and responsibilities without being asked.,1-5,5
5.2,KRA-5,Shows a commitment to continuous learning and skill development.,1-5,5
```

### **Step 3: How to Import into ERPNext**

1.  **Create the Template Header:**
    *   Go to `Human Resources > Appraisal > Appraisal Template > New`.
    *   **Title:** `Software Engineer - Annual Review`
    *   **Description:** `Annual performance appraisal for Software Engineers.`
    *   **Save** the new template. (Note its name, e.g., `APP-TMP-00001`).

2.  **Import the KRAs:**
    *   In the saved template, find the **Goals (KRAs)** table.
    *   Click the menu icon (⋮) in the table header and select **Import**.
    *   Upload the `appraisal_kras.csv` file.
    *   **Map the columns:**
        *   `id` -> `ID`
        *   `kra` -> `KRA`
        *   `per_weightage` -> `Per Weightage (%)`
    *   Click **Import**.

3.  **Import the Rating Criteria:**
    *   In the same template, find the **Rating Criteria** table.
    *   Click the menu icon (⋮) and select **Import**.
    *   Upload the `appraisal_criteria.csv` file.
    *   **Map the columns:**
        *   `id` -> `ID`
        *   `parent` -> `Parent` (This links each criterion to its KRA ID)
        *   `criteria` -> `Criteria`
        *   `rating` -> `Rating`
        *   `per_weightage` -> `Per Weightage (%)`
    *   Click **Import**.

4.  **Verify and Save:**
    *   Check that all KRAs and Criteria were imported correctly and that the total weightage sums to 100.
    *   Click **Save**.

You can now use this template to create appraisals for your Software Engineers! This same CSV structure can be easily adapted for any other role.