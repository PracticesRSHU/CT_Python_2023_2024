<h1>Things to bring to our picnic</h1>
{{rows}}
<table>
   <tbody>
       <tr><th>Item</th><th>Counts</th></tr>
       %for row in rows:
       <tr>
          %for col in row:
           <td>{{col}}</td>
          %end
       </tr>
       %end
   <tbody>
</table>