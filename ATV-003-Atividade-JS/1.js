// 1. Duração em segundos para horas, minutos e segundos
let seg = 3665;

let h = Math.floor(seg / 3600);
let m = Math.floor((seg % 3600) / 60);
let s = seg % 60;

console.log(`${h}h ${m}min ${s}s`);
