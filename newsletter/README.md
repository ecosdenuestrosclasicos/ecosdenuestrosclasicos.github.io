# Newsletter semanal

- `notas.md`: lo que Isa quiere contar cada semana, con fecha.
- El correo lo genera `scripts/newsletter.mjs` y lo envía el flujo `.github/workflows/newsletter.yml` los lunes por la mañana.
- Vista previa en el ordenador: `node scripts/newsletter.mjs semanal --vista` y abre `newsletter/vista-semanal.html`.
- Pausa: crea el archivo `newsletter/PAUSA`.
