
/**
 * Lecture V2: regenerate all 11 source-based SVGs.
 * Only Node.js built-ins. No simulations and no raw per-seed shards.
 * Run: node generate_v2_figures.mjs (from any directory).
 */
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const here=path.dirname(fileURLToPath(import.meta.url));
const src=path.resolve(here,'../../../results/pooled_loocv_smoothness/process_examples/seed_study_1000_v1');
const parse=(s)=>{const lines=s.trim().split(/\r?\n/),keys=lines.shift().split(',');return lines.map(x=>Object.fromEntries(x.split(',').map((v,i)=>[keys[i],v])));};
const risk=parse(fs.readFileSync(path.join(src,'risk_by_process_method.csv'),'utf8'));
const pools=parse(fs.readFileSync(path.join(src,'paired_pooling_first_series.csv'),'utf8'));
const cases=[...new Set(risk.map(x=>x.case))];
const methods=[...new Set(risk.map(x=>x.method))];
const query=(c,m,R)=>risk.find(x=>x.case===c&&x.method===m&&x.R===String(R));
const esc=(s)=>String(s).replaceAll('&','&amp;').replaceAll('<','&lt;');
const label=(x,y,v,size=15,c='#20354b',anchor='start')=>'<text x="'+x+'" y="'+y+'" font-family="Arial" text-anchor="'+anchor+'" font-size="'+size+'" fill="'+c+'">'+esc(v)+'</text>';
const rect=(x,y,w,h,c)=>'<rect x="'+x+'" y="'+y+'" width="'+w+'" height="'+h+'" rx="5" fill="'+c+'"/>';
const line=(x,y,u,v,col='#20354b',w=2)=>'<line x1="'+x+'" y1="'+y+'" x2="'+u+'" y2="'+v+'" stroke="'+col+'" stroke-width="'+w+'"/>';
const page=(title,subtitle,content)=>'<svg xmlns="http://www.w3.org/2000/svg" width="1250" height="720"><rect width="1250" height="720" fill="white"/>'+rect(0,0,11,720,'#168a89')+label(45,57,title,32)+label(45,93,subtitle,18,'#536777')+content+label(45,679,'Source: Study M.2 committed CSV summaries; descriptive reconstruction statistics.',15,'#536777')+'</svg>\n';
const out={};

for(const R of [1,3]){
 for(const [metric,slug] of [['ex_post_seed_win_fraction','win_frequency'],['median_selected_s_nominal','selected_s']]){
   let body='',x0=270,y0=185,w=79,h=42;
   methods.forEach((m,j)=>body+=label(x0+j*w+w/2,164,m.slice(0,9),13,'#20354b','middle'));
   cases.forEach((c,i)=>{
     body+=label(252,y0+i*h+26,c.replaceAll('_',' '),17,'#20354b','end');
     methods.forEach((m,j)=>{
       const v=Number(query(c,m,R)[metric]),z=Math.max(0,Math.min(1,v)),col='rgb('+Math.round(239-196*z)+','+Math.round(247-132*z)+','+Math.round(250-121*z)+')';
       body+=rect(x0+j*w,y0+i*h,w-3,h-3,col);
       body+=label(x0+j*w+w/2,y0+i*h+26,metric==='ex_post_seed_win_fraction'?(100*v).toFixed(1)+'%':v.toFixed(2),13,z>.6?'white':'#20354b','middle');
     });
   });
   body+=label(50,625,metric==='ex_post_seed_win_fraction'?'Seed win is ex-post and NOT a deployable policy.':'Nominal S is not the pooled fitted-mean EDF.',19,'#536777');
   out['v2_'+slug+'_R'+R+'.svg']=page(slug.replaceAll('_',' ')+' · R='+R,'Nine processes × eleven methods, 1000 independent seeds',body);
 }
}
{
 let body='',x0=270,y0=184,w=79,h=42;
 methods.forEach((m,j)=>body+=label(x0+j*w+w/2,160,m.slice(0,9),13,'#20354b','middle'));
 cases.forEach((c,i)=>{
   body+=label(251,y0+i*h+25,c.replaceAll('_',' '),17,'#20354b','end');
   methods.forEach((m,j)=>{
     const v=Number(query(c,m,3).mean_fitted_mu);
     body+=rect(x0+j*w,y0+i*h,w-3,h-3,v===0?'#e0e4ea':v<.035?'#c8e7fa':'#d6f0e6');
     body+=label(x0+j*w+w/2,y0+i*h+26,v.toFixed(3),14,'#20354b','middle');
   });
 });
 body+=label(50,621,'Gaussian reference difference mean = 0.04; zero policies force μ=0.',18,'#536777');
 out['v2_fitted_mu_R3.svg']=page('Fitted mean of differences — R3','Mean estimated μ by method and process',body);
}
{
 let body='';
 cases.forEach((c,i)=>{
   body+=label(238,170+i*49+23,c.replaceAll('_',' '),17,'#20354b','end');
   methods.map(m=>query(c,m,3)).sort((a,b)=>Number(a.mean_pool_mse)-Number(b.mean_pool_mse)).slice(0,4).forEach((row,j)=>{
     const x=253+j*233,y=170+i*49;
     body+=rect(x,y,222,37,j===0?'#d9f1e8':'#edf4f8');
     body+=label(x+8,y+24,(j+1)+'. '+row.method.slice(0,10)+' '+Number(row.mean_pool_mse).toFixed(4),14);
   });
 });
 body+=label(50,633,'Mean-MSE ranks do not encode Holm significance.',19,'#bd5260');
 out['v2_ranking_ladder_R3.svg']=page('Four lowest-risk policies by process','R3, sample mean latent MSE; all 11 policies still appear in the full appendix',body);
}
for(const method of ['cv_joint','aicc_joint','plugin_mu_ml']){
 const map=v=>560+7800*v;
 let body=line(map(0),150,map(0),574,'#bd5260',3);
 cases.forEach((c,i)=>{
   const q=pools.find(x=>x.case===c&&x.method===method),y=174+i*46;
   const v=Number(q.mean_first_series_mse_R3_minus_R1_negative_favors_pooling);
   body+=label(296,y+6,c.replaceAll('_',' '),17,'#20354b','end');
   body+=line(map(Number(q.ci95_low_pointwise)),y,map(Number(q.ci95_high_pointwise)),y);
   body+='<circle cx="'+map(v)+'" cy="'+y+'" r="7" fill="'+(v>0?'#bd5260':'#16846c')+'"/>';
   body+=label(1080,y+6,(v>0?'+':'')+v.toFixed(4),17,v>0?'#bd5260':'#16846c');
 });
 body+=label(60,613,'Negative: pooling helps first series. Positive: pooling harms.',19,'#536777');
 out['v2_pooling_forest_'+method+'.svg']=page('First-series pooling effect: '+method,'Paired first-series R3−R1 mean MSE and 95% pointwise CIs',body);
}
for(const R of [1,3]){
 const c=['observation_outliers','ar1_observation','level_jump'],palette=['#2864a2','#bc5261','#16846c'];
 const d=risk.filter(z=>z.R===String(R)&&c.includes(z.case));
 const max=Math.max(...d.map(z=>Number(z.p90_pool_mse)))*1.08;
 let body=line(120,559,1090,559)+line(120,559,120,173);
 d.forEach(z=>{
   const x=120+Number(z.mean_pool_mse)/max*960,y=550-Number(z.p90_pool_mse)/max*345,fill=palette[c.indexOf(z.case)];
   body+='<circle cx="'+x+'" cy="'+y+'" r="6" fill="'+fill+'" opacity=".8"><title>'+esc(z.case+' '+z.method)+'</title></circle>';
 });
 body+=label(412,605,'Mean latent MSE →',20)+label(130,163,'Higher p90 = worse tail',19,'#536777');
 c.forEach((name,i)=>{body+=rect(135+i*330,635,17,13,palette[i])+label(160+i*330,649,name.replaceAll('_',' '),15);});
 out['v2_mean_vs_p90_R'+R+'.svg']=page('Mean loss versus upper-tail loss · R='+R,'Three selected mechanisms, eleven policies per mechanism',body);
}
const dest=path.join(here,'assets');fs.mkdirSync(dest,{recursive:true});
for(const [name,data] of Object.entries(out))fs.writeFileSync(path.join(dest,name),data,'utf8');
console.log('Regenerated',Object.keys(out).length,'Lecture V2 SVG charts');
