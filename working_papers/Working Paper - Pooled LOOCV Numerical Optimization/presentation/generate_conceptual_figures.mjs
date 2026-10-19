// Regenerate lecture-specific conceptual SVGs without Python or external packages.
// Run from anywhere: node generate_conceptual_figures.mjs
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
function concepts(){
 const N="#142c4a",T="#1f888c",B="#2a63a1",R="#bf5360",G="#e9f5f6",K="#61768b";
 const tx=(x,y,s,z=25,c=N)=>`<text x="${x}" y="${y}" font-family="Arial, sans-serif" fill="${c}" font-size="${z}">${s}</text>`;
 const rc=(x,y,w,h,c,r=8)=>`<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="${r}" fill="${c}"/>`;
 const ln=(x,y,u,v,c=N,sw=3)=>`<line x1="${x}" y1="${y}" x2="${u}" y2="${v}" stroke="${c}" stroke-width="${sw}"/>`;
 const pth=(pts,c,w=4)=>`<polyline points="${pts}" fill="none" stroke="${c}" stroke-width="${w}" stroke-linejoin="round"/>`;
 const page=(title,sub,x)=>`<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="675" viewBox="0 0 1200 675">${rc(0,0,1200,675,"#fff",0)}${rc(0,0,12,675,T,0)}${tx(53,58,title,34,N)}${tx(53,95,sub,18,K)}${x}${ln(53,633,1147,633,"#dde6eb",2)}${tx(55,657,"Teaching diagram · conceptual unless a source table is named",14,K)}</svg>\n`;
 const pts=(fn,x0=100,y0=200,w=1000,h=340)=>Array.from({length:101},(_,k)=>{let t=k/100;return `${(x0+t*w).toFixed(1)},${(y0+h*fn(t)).toFixed(1)}`}).join(" ");
 const ans={};
 {
 let c=rc(80,175,1040,410,G,16);
 let f=t=>.62+.11*Math.sin(2*Math.PI*t*2)-.25*t;
 c+=pth(pts(f,100,197,1000,350),T,6);
 for(let i=0;i<76;i++){let t=i/75,x=100+1000*t,y=197+350*(f(t)+.07*Math.sin(71*t)+.045*Math.cos(127*t));c+=`<circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="3.4" fill="${B}" opacity=".67"/>`;}
 c+=tx(104,562,"Teal = latent trend τ",23,T)+tx(505,562,"Blue dots = observed y = τ + η",23,B);
 ans["01_observed_vs_latent.svg"]=page("What are we trying to reconstruct?","Signal and noisy measurements (a teaching schematic, not a Monte Carlo draw)",c);
 }
 {
 let c=tx(69,152,"Five rows, seven columns",26,N);
 let a=[[1,-2,1,0,0,0,0],[0,1,-2,1,0,0,0],[0,0,1,-2,1,0,0],[0,0,0,1,-2,1,0],[0,0,0,0,1,-2,1]];
 for(let i=0;i<5;i++)for(let j=0;j<7;j++){let v=a[i][j],x=68+j*78,y=184+i*72;c+=rc(x,y,67,60,v===-2?R:v===1?T:G,6);c+=tx(x+24,y+40,String(v),25,v===0?K:"#fff")}
 c+=tx(710,240,"Q = D₂ᵀD₂",38,N)+tx(710,315,"rank(Q) = N − 2",31,T)+tx(710,376,"dim ker(Q) = 2",29,N)+tx(710,448,"Unpenalized: a + bt",26,B);
 ans["02_d2_matrix.svg"]=page("Second differences become a penalty matrix","The two zero eigenvalues correspond to an intercept and a linear trend",c);
 }
 {
 let c=ln(116,538,1080,538,N,2)+ln(116,203,116,538,N,2);
 const sets=[[.03,T],[.3,B],[2,R]];
 for(let [lam,col] of sets){let z=pts(t=>1-1/(1+lam*30*t),116,211,947,300);c+=pth(z,col,5);}
 c+=tx(90,220,"1",18,K)+tx(87,540,"0",18,K)+tx(1050,577,"q →",20,K);
 sets.forEach(([lam,col],i)=>{c+=ln(530,143+i*27,574,143+i*27,col,5)+tx(587,150+i*27,"λ = "+lam,19,col)});
 c+=tx(177,603,"Spectral response = 1 / (1 + λq)",26,N);
 ans["03_spectral_shrinkage.svg"]=page("Why increasing λ suppresses roughness","An exact spectral-transfer formula on an illustrative eigenvalue axis",c);
 }
 {
 let c=tx(71,156,"One independent seed j",26,B)+rc(66,175,315,99,G)+tx(94,235,"εʲ, ηʲ, zʲ",32,N);
 c+=ln(391,224,528,224,B,5)+tx(544,233,"9 modified processes",30,N);
 for(let i=0;i<9;i++){let x=62+i*123;c+=rc(x,338,104,73,i%3===0?"#e1eef9":i%3===1?"#e1f3ee":"#fbeaea",12);c+=tx(x+40,388,String(i+1),28,N);}
 c+=tx(74,480,"Each process → R=1, R=3 → 11 feasible policies",27,N);
 c+=tx(74,565,"1,000 independent seeds ≠ 198,000 independent observations",26,R);
 ans["04_common_seed_design.svg"]=page("Same random shocks, nine mechanisms, eleven policies","One seed is the statistical unit; everything within it is paired",c);
 }
 {
 let c=tx(80,150,"First series is identical in both fits",31,N);
 c+=tx(145,225,"R = 1",30,B)+tx(775,225,"R = 3",30,T);
 c+=rc(69,265,470,103,G,17)+tx(95,329,"y¹ → λ̂¹ → τ̂¹",32,B);
 for(let i=0;i<3;i++){let y=265+i*104;c+=rc(649,y,483,88,i===0?"#e0f4f0":G,14);c+=tx(685,y+54,"y"+(i+1)+" → shared λ̂ → τ̂"+(i+1),27,N)}
 c+=tx(82,572,"Only the additional series—and hence fitted common λ—change.",24,R);
 ans["05_pooled_parameter_logic.svg"]=page("Pooling: compare reconstruction of the SAME first series","A common λ can change the fitted first trend even though y¹ never changes",c);
 }
 return ans;
}
const dir=path.join(path.dirname(fileURLToPath(import.meta.url)),'assets');
fs.mkdirSync(dir,{recursive:true});
for(const [name,svg] of Object.entries(concepts()))fs.writeFileSync(path.join(dir,name),svg,'utf8');
console.log('Generated '+Object.keys(concepts()).length+' teaching figures');
