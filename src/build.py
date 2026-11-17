#!/usr/bin/env python3
"""Reproducible fictional luxury AI governance portfolio. Python 3.9+, standard library."""
import csv
import json
import random
import sqlite3
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "outputs"
DATA.mkdir(exist_ok=True)
OUT.mkdir(exist_ok=True)
SEED = 20261117
rng = random.Random(SEED)

USE_CASES = [
 ("Personal styling recommender","Retail","Recommendation","Customer preferences",3,3,2,2,3),
 ("VIP client segmentation","Clienteling","Profiling","Purchase history",4,4,3,3,4),
 ("Fragrance discovery assistant","Beauty","Conversational AI","Preferences",2,2,2,2,2),
 ("AI fashion campaign generator","Marketing","Generative AI","Creative assets",2,3,3,2,3),
 ("Luxury handbag authentication","Resale","Computer vision","Product images",4,4,3,4,3),
 ("Candidate screening assistant","People","Employment","Applicant profiles",5,5,4,4,4),
 ("Boutique staffing forecast","Operations","Forecasting","Store schedules",3,3,2,2,3),
 ("Fraud review triage","Payments","Decision support","Transactions",4,4,4,4,3),
 ("Product copy generator","Ecommerce","Generative AI","Catalog text",1,2,2,1,2),
 ("Customer service summarizer","Service","Summarization","Support tickets",3,3,3,2,3),
 ("Inventory demand forecast","Supply chain","Forecasting","Inventory records",2,2,1,2,2),
 ("Dynamic offer targeting","Marketing","Profiling","Behavioral events",4,4,3,3,4),
 ("Jewelry visual search","Jewelry","Computer vision","Product images",2,2,2,1,2),
 ("Returns anomaly detector","Operations","Anomaly detection","Returns history",3,3,2,3,3),
 ("Influencer campaign selector","Marketing","Ranking","Creator profiles",3,3,3,3,3),
 ("Product review summarizer","Beauty","Summarization","Product reviews",2,3,3,2,3),
 ("Made-to-order lead time predictor","Atelier","Forecasting","Production schedules",2,2,1,2,2),
 ("Luxury resale price estimator","Resale","Prediction","Market listings",3,3,2,3,2),
 ("Customer churn predictor","Clienteling","Prediction","Purchase history",4,4,3,3,3),
 ("Employee learning recommender","People","Recommendation","Training records",3,3,2,2,2),
 ("Virtual try-on assistant","Retail","Computer vision","Customer photos",4,4,3,3,4),
 ("Sustainability claims checker","Compliance","Document analysis","Supplier disclosures",3,4,3,3,3),
 ("Supplier due diligence assistant","Procurement","Document analysis","Vendor records",3,3,3,3,3),
 ("Boutique footfall predictor","Retail","Forecasting","Aggregate traffic",1,2,1,2,2),
]
WEIGHTS = {"impact":.30,"data_sensitivity":.25,"autonomy":.20,"scale":.15,"opacity":.10}

def risk_score(values):
    """Internal 20-100 prioritization rubric, NOT an EU AI Act classification."""
    return round(sum(values[k] * WEIGHTS[k] for k in WEIGHTS) / 5 * 100)

def risk_tier(score):
    return "High" if score >= 70 else "Medium" if score >= 45 else "Low"

def write_csv(path, rows, fields):
    with path.open("w",newline="",encoding="utf-8") as file:
        writer = csv.DictWriter(file,fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

def main():
    systems=[]
    for i,(name,department,kind,data_type,impact,sensitivity,autonomy,scale,opacity) in enumerate(USE_CASES,1):
        dimensions=dict(impact=impact,data_sensitivity=sensitivity,autonomy=autonomy,scale=scale,opacity=opacity)
        score=risk_score(dimensions)
        systems.append(dict(system_id=f"AI-{i:03d}",name=name,department=department,system_type=kind,data_type=data_type,**dimensions,risk_score=score,risk_tier=risk_tier(score),owner=f"{department} Governance Lead",deployment_status=rng.choice(["Pilot","Production","Design review"]),legal_review_status=rng.choice(["Pending","In progress","Reviewed"]),simulated=1))

    controls=[
        ("GOV-01","Document intended purpose and business owner","NIST AI RMF","Govern"),
        ("GOV-02","Maintain AI system inventory and risk rationale","NIST AI RMF","Govern"),
        ("MAP-01","Document data sources and affected stakeholders","NIST AI RMF","Map"),
        ("MEA-01","Evaluate quality, reliability and subgroup outcomes","NIST AI RMF","Measure"),
        ("MAN-01","Define human review and escalation pathways","NIST AI RMF","Manage"),
        ("PRV-01","Assess lawful basis and data minimization where GDPR applies","GDPR","Articles 5–6"),
        ("PRV-02","Assess DPIA trigger where GDPR applies","GDPR","Article 35"),
        ("AIA-01","Determine actor role and prohibited-practice applicability","EU AI Act","Article 5 / actor roles"),
        ("AIA-02","Assess high-risk classification based on intended use","EU AI Act","Article 6 / Annex III"),
        ("AIA-03","Review applicable transparency duties and effective dates","EU AI Act","Article 50"),
        ("AIA-04","Assess provider/deployer obligations if classified high-risk","EU AI Act","Applicable provisions")
    ]
    assessments=[]
    for s in systems:
        for cid,_,framework,_ in controls:
            status=rng.choices(["Implemented","Partial","Missing","Not assessed"],weights=[42,28,18,12])[0]
            assessments.append(dict(system_id=s["system_id"],control_id=cid,framework=framework,status=status,finding_id=f'F-{s["system_id"][3:]}-{cid}',simulated=1))

    groups=["Group A","Group B","Group C"]
    probabilities={"Group A":.68,"Group B":.57,"Group C":.62}
    audit=[]
    for n in range(2400):
        group=groups[n%3]
        qualified=int(rng.random()<.55)
        p=probabilities[group] if qualified else probabilities[group]*.43
        selected=int(rng.random()<p)
        audit.append(dict(case_id=f"CASE-{n+1:04d}",group_label=group,eligible_proxy=qualified,positive_decision=selected,model_id="AI-012",simulated=1))

    aggregates=defaultdict(lambda: dict(n=0,positive=0,eligible=0,eligible_positive=0))
    for case in audit:
        a=aggregates[case["group_label"]]
        a["n"]+=1
        a["positive"]+=case["positive_decision"]
        if case["eligible_proxy"]:
            a["eligible"]+=1
            a["eligible_positive"]+=case["positive_decision"]
    fairness=[]
    for group,a in sorted(aggregates.items()):
        fairness.append(dict(group=group,sample_size=a["n"],positive_count=a["positive"],selection_rate=round(a["positive"]/a["n"],4),eligible_count=a["eligible"],true_positive_rate_proxy=round(a["eligible_positive"]/a["eligible"],4) if a["eligible"] else None))
    rates=[x["selection_rate"] for x in fairness]
    fairness_summary=dict(max_selection_rate_gap_pp=round((max(rates)-min(rates))*100,2),min_to_max_selection_ratio=round(min(rates)/max(rates),3) if max(rates) else None,interpretation="Screening signal only. No legal or causal conclusion.")

    write_csv(DATA/"systems.csv",systems,list(systems[0]))
    write_csv(DATA/"controls.csv",[dict(control_id=x[0],control_name=x[1],framework=x[2],reference=x[3]) for x in controls],["control_id","control_name","framework","reference"])
    write_csv(DATA/"assessments.csv",assessments,list(assessments[0]))
    write_csv(DATA/"fairness_audit.csv",audit,list(audit[0]))
    write_csv(OUT/"fairness_metrics.csv",fairness,list(fairness[0]))

    database=sqlite3.connect(OUT/"maison_ethique.sqlite")
    for name,rows in [("systems",systems),("assessments",assessments),("fairness_audit",audit)]:
        database.execute(f"DROP TABLE IF EXISTS {name}")
        fields=list(rows[0])
        types=["INTEGER" if isinstance(rows[0][key],int) else "REAL" if isinstance(rows[0][key],float) else "TEXT" for key in fields]
        database.execute(f'CREATE TABLE {name} ('+", ".join(f"{key} {type_}" for key,type_ in zip(fields,types))+")")
        database.executemany(f'INSERT INTO {name} VALUES ('+",".join("?" for _ in fields)+")",[[row[key] for key in fields] for row in rows])
    database.commit()
    database.close()

    summary=dict(title="Maison Éthique | The AI Risk Atelier",synthetic=True,seed=SEED,system_count=len(systems),high_risk_count=sum(s["risk_tier"]=="High" for s in systems),controls_total=len(assessments),controls_implemented=sum(a["status"]=="Implemented" for a in assessments),open_findings=sum(a["status"] in ("Missing","Partial") for a in assessments),fairness=fairness_summary)
    (OUT/"summary.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")
    payload=dict(summary=summary,systems=systems,controls=assessments,fairness=fairness,regulatory=[
        dict(framework="NIST AI RMF",type="Voluntary framework",note="Govern, Map, Measure, Manage; voluntary guidance, not a certification."),
        dict(framework="GDPR",type="Binding where applicable",note="Obligations depend on jurisdiction, roles, processing and lawful basis."),
        dict(framework="EU AI Act",type="Binding where applicable; phased implementation",note="Classify by intended purpose, actor role and dates. Internal score is not statutory classification.")])
    template=(ROOT/"dashboard"/"template.html").read_text(encoding="utf-8")
    embedded=json.dumps(payload,ensure_ascii=True).replace("</","<\\/")
    (ROOT/"dashboard"/"index.html").write_text(template.replace("/*__PAYLOAD__*/",embedded),encoding="utf-8")
    print(f"Built {len(systems)} fictional AI systems, {len(assessments)} assessments, {len(audit)} fairness cases.")
    print("Open dashboard/index.html")

if __name__=="__main__":
    main()
