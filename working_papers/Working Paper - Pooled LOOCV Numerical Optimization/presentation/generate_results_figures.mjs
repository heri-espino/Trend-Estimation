// Rebuild lecture-specific RISK figures using ONLY committed compact CSVs.
// No raw Monte Carlo shards, Python packages, or browser dependencies needed.
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url));
const base=path.resolve(here,'../../../results/pooled_loocv_smoothness/process_examples');
function csv(s){let rows=s.trim().split(/\r?\n/),header=rows.shift().split(",");return rows.map(line=>Object.fromEntries(line.split(",").map((v,i)=>[header[i],v])));}
function figures(risk,pairs,pool,gallery){
const N="#142c4a",B="#27659d",T="#16898b",R="#ba5260",G="#ebf5f6",K="#64748a",O="#efa845";
const txt=(x,y,s,z=21,col=N,weight="normal",align="start")=>`<text x="${x}" y="${y}" font-size="${z}" font-family="Arial,sans-serif" text-anchor="${align}" font-weight="${weight}" fill="${col}">${String(s).replaceAll("&","&amp;")}</text>`;
const rect=(x,y,w,h,c,rx=7)=>`<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="${rx}" fill="${c}"/>`;
const line=(x,y,u,v,c=N,w=2,dash="")=>`<line x1="${x}" y1="${y}" x2="${u}" y2="${v}" stroke="${c}" stroke-width="${w}" ${dash?'stroke-dasharray="'+dash+'"':""}/>`;
const circle=(x,y,r,c)=>`<circle cx="${x}" cy="${y}" r="${r}" fill="${c}"/>`;
const chart=(title,sub,body,note)=>`<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="675" viewBox="0 0 1200 675">${rect(0,0,1200,675,"#fff",0)}${rect(0,0,12,675,T,0)}${txt(50,59,title,33,N,"bold")}${txt(50,96,sub,18,K)}${body}${line(53,633,1147,633,"#dae5eb")}${txt(53,655,note,14,K)}</svg>\n`;
const cases=["gaussian_reference","smooth_cycle","slope_break","level_jump","observation_outliers","ar1_observation","variance_regime","heterogeneous_pool","shared_observation_shock"];
const names=["Gaussian reference","Smooth cycle","Slope break","True level jump","Observation outliers","AR(1) observation","Variance regime","Unequal series SD","Shared noise shock"];
const get=(c,r,m)=>risk.find(x=>x.case===c&&x.R===String(r)&&x.method===m);
const out={};
{
 let c="";
 for(let i=0;i<cases.length;i++){let caseName=cases[i],rs=risk.filter(x=>x.case===caseName&&x.R==="3").sort((a,b)=>+a.mean_pool_mse-+b.mean_pool_mse),d=(+rs[1].mean_pool_mse-(+rs[0].mean_pool_mse))/(+rs[1].mean_pool_mse)*100;
 let p=pairs.find(x=>x.case===caseName&&x.R==="3"&&((x.method_A===rs[0].method&&x.method_B===rs[1].method)||(x.method_B===rs[0].method&&x.method_A===rs[1].method))),sig=+p.paired_t_p_holm_all_processes<.05,y=150+i*49;
 c+=txt(265,y+22,names[i],20,N,"normal","end")+rect(290,y,Math.max(2,d*125),31,sig?R:B,4)+txt(300+d*125,y+23,d.toFixed(2)+"%"+(sig?" ★":""),18,sig?R:N,"bold");
 }
 c+=txt(74,613,"★ = significant AFTER one global Holm correction over 990 method-pair tests",18,R);
 out["06_runner_up_gaps.svg"]=chart("Top vs runner-up: practical margin and uncertainty","Relative mean-MSE gain of lowest policy over the second-lowest, R = 3",c,"Source: committed risk and matched-pair Holm CSVs; no invented raw seeds");
}
{
 const policies=["gcv_joint","cv_joint","gls_mu_ml","aicc_joint","controlled_s0.8_joint"],colors=[R,B,O,"#805eb7",T];
 let c=rect(101,160,1005,391,G,12)+line(151,515,1081,515,N)+line(151,188,151,515,N);
 for(let i=0;i<policies.length;i++){let z=get("ar1_observation",3,policies[i]),s=+z.median_selected_s_nominal,m=+z.mean_pool_mse,x=151+(s-.35)/.52*909,y=505-(m-.48)/.12*300;
 c+=circle(x,y,10,colors[i]);c+=txt(x+(i%2===0?12:-13),y+(i%2===0?-14:28),policies[i].replaceAll("_"," "),18,colors[i],"bold",i%2===0?"start":"end");}
 c+=txt(630,586,"Median nominal smoothness S",23,N,"bold","middle")+txt(65,199,"Higher MSE",19,K);
 out["07_ar1_s_vs_mse.svg"]=chart("AR(1) observation noise: selected S versus actual latent risk","Each dot is one of five policies, not a separate realization",c,"Data: 1000 seeds · phi=.85 · R3 · no smoothness policy tuned on true tau");
}
{
 let c="";const ms=["controlled_s0.5_joint","gcv_zero","cv_joint","aicc_joint","gls_mu_ml"];
 ms.forEach((m,i)=>{let v=+get("level_jump",3,m).mean_pool_mse,y=180+i*78,w=(v/.46)*730;
 c+=txt(325,y+34,m.replaceAll("_"," "),19,N,"normal","end")+rect(348,y,w,51,i===0?T:i===4?R:B,6)+txt(359+w,y+34,v.toFixed(5),21,N,"bold");});
 out["08_level_jump_risk.svg"]=chart("True level jump: less smoothing can reduce reconstruction bias","R3 mean MSE for representative feasible selectors",c,"Amplitude +7 · source: 1000-seed R3 aggregate conditional risk");
}
{
 const ms=["aicc_joint","plugin_mu_ml","gls_mu_ml","cv_joint"],colors=[T,B,R],lab=["median","mean","p90"];
 let c=txt(87,158,"Error scale 0–0.72",20,K);
 ms.forEach((m,i)=>{let r=get("observation_outliers",1,m),values=[+r.median_pool_mse,+r.mean_pool_mse,+r.p90_pool_mse],x=165+i*249;
 values.forEach((v,j)=>{let h=v/.72*310;c+=rect(x+j*47,519-h,35,h,colors[j],4);});
 c+=txt(x+75,564,m.replaceAll("_"," "),17,N,"normal","middle");
 });
 lab.forEach((l,i)=>{c+=rect(200+i*210,604,19,14,colors[i],2)+txt(227+i*210,617,l,18,colors[i],"bold");});
 out["09_outlier_tail_summary.svg"]=chart("Outliers: average loss hides the unstable tail","R1; median, mean and 90th-percentile seed MSE are independently archived",c,"Source: risk_by_process_method.csv; distribution summary, NOT raw boxplots");
}
{
 let c="",lo=-.135,hi=.035,map=v=>280+(v-lo)/(hi-lo)*760;
 c+=line(map(0),145,map(0),569,R,3,"7 7")+txt(map(0)+7,152,"No change",16,R);
 cases.forEach((name,i)=>{let p=pool.find(x=>x.case===name&&x.method==="gls_mu_ml"),a=+p.ci95_low_pointwise,b=+p.ci95_high_pointwise,v=+p.mean_first_series_mse_R3_minus_R1_negative_favors_pooling,y=185+i*44;
 c+=txt(260,y+6,names[i],17,N,"normal","end")+line(map(a),y,map(b),y,N,4)+line(map(a),y-7,map(a),y+7,N)+line(map(b),y-7,map(b),y+7,N)+circle(map(v),y,7,v>0?R:T)+txt(1061,y+7,(v>0?"+":"")+v.toFixed(4),18,v>0?R:T,"bold");});
 c+=txt(280,600,"Left of 0 = pooling helps first series",18,T)+txt(758,600,"Right of 0 = pooling harms",18,R);
 out["10_first_series_pooling_forest.svg"]=chart("Pooling: first-series reconstruction may improve or deteriorate","GLS/ML mean paired MSE difference R3 − R1 with pointwise 95% CI",c,"Data: paired_pooling_first_series.csv · identical first y, same seed");
}
{
 let c=txt(120,154,"SD of observational noise: 0.25 / 0.80 / 1.50",23,N);
 const ms=["plugin_mu_ml","gls_mu_ml","cv_joint","controlled_s0.8_joint"];
 for(let i=0;i<ms.length;i++){let m=ms[i],one=+get("heterogeneous_pool",1,m).mean_first_series_mse,three=+get("heterogeneous_pool",3,m).mean_first_series_mse,x=180+i*240,h1=one/.055*300,h3=three/.055*300;
 c+=rect(x,531-h1,64,h1,B,5)+rect(x+74,531-h3,64,h3,R,5)+txt(x+34,518-h1,one.toFixed(3),17,B,"bold","middle")+txt(x+105,518-h3,three.toFixed(3),17,R,"bold","middle")+txt(x+72,576,m.replaceAll("_"," "),17,N,"normal","middle");}
 c+=rect(190,604,18,14,B,3)+txt(217,617,"R1",17,N)+rect(330,604,18,14,R,3)+txt(357,617,"R3",17,N);
 out["11_heterogeneous_clean_series.svg"]=chart("The cleanest series can be harmed by pooling","MSE of EXACTLY the same first series under a common selected lambda",c,"Source: first-series MSE across 1000 matched seeds, not pooled three-series mean");
}
{
 let matches=0,c="";
 gallery.forEach((g,i)=>{let sel=risk.filter(x=>x.case===g.case&&x.R===g.R).sort((a,b)=>+a.mean_pool_mse-+b.mean_pool_mse)[0].method,yes=sel===g.lowest_MSE_in_THIS_ONE_realization_NOT_DEPLOYABLE_SELECTOR;matches+=+yes;
 let x=75+(i%9)*120,y=192+Math.floor(i/9)*127;c+=rect(x,y,99,93,yes?"#dbf2e9":"#f9e2e5",12)+txt(x+51,y+59,yes?"YES":"NO",23,yes?T:R,"bold","middle");});
 c+=txt(80,531,matches+"/18",55,N,"bold")+txt(267,528,"single-seed winners matched the lowest mean-MSE policy.",23,N);
 c+=txt(80,590,"Rows: R1 and R3; columns: nine mechanisms. This is descriptive agreement.",19,K);
 out["12_one_seed_vs_1000.svg"]=chart("Why we needed 1,000 independent seeds","Each tile compares one gallery winner with the lowest 1000-seed mean-MSE policy",c,"Sources: gallery_001/illustrative_winners.csv and seed_study_1000_v1/risk_by_process_method.csv");
}
return out;
}
const read=(relative)=>csv(fs.readFileSync(path.join(base,relative),'utf8'));
const pictures=figures(read('seed_study_1000_v1/risk_by_process_method.csv'),read('seed_study_1000_v1/paired_method_mse_differences.csv'),read('seed_study_1000_v1/paired_pooling_first_series.csv'),read('gallery_001/illustrative_winners.csv'));
const dest=path.join(here,'assets');fs.mkdirSync(dest,{recursive:true});
for(const [name,svg] of Object.entries(pictures))fs.writeFileSync(path.join(dest,name),svg,'utf8');
console.log('Generated '+Object.keys(pictures).length+' empirical SVGs');
