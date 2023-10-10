
$('.plus-cart').click(function(){
  var id = $(this).attr('pid').toString();
  var quantia = this.parentNode.children[2]
  $.ajax({
     type:"GET",
     url:"/plus_cart",
     data:{
       prod_id:id
     },
     success:function(data) {
       console.log('data=',data);
       quantia.innerText=data.quantidade;
       total = document.getElementById('total').innerHTML = '<strong> R$ '+data.total +',00  REAIS </strong>';
       total_tudo = document.getElementById('total_tudo').innerHTML='<strong> R$ '+data.total_tudo +',00  REAIS </strong>';
     }
   })
  })

$('.minus-cart').click(function(){
  var id = $(this).attr('pid').toString();
  var quantia = this.parentNode.children[2]
  $.ajax({
     type:"GET",
     url:"/minus_cart",
     data:{
       prod_id:id
     },
     success:function(data) {
       console.log('data=',data);
       quantia.innerText=data.quantidade;
       total = document.getElementById('total').innerHTML = '<strong> R$ '+data.total +',00  REAIS </strong>';
       total_tudo = document.getElementById('total_tudo').innerHTML='<strong> R$ '+data.total_tudo +',00  REAIS </strong>';

     }
   })
  })


$('.remove-cart').click(function(){
  var id = $(this).attr('pid').toString();
  var eml= this
  $.ajax({
     type:"GET",
     url:"/remove_cart",
     data:{
       prod_id:id
     },
     success:function(data) {
       document.getElementById('total').innerText = data.total
       document.getElementById('total_tudo').innerText= data.total_tudo
       eml.parentNode.remove()
       eml.preventDefault()
     }
   })
  })


$('.remove-desejo').click(function(){
  var id = $(this).attr('pid').toString();
  var eml= this
  $.ajax({
     type:"GET",
     url:"/remove_desejo",
     data:{
       prod_id:id
     },
     success:function(data) {
       eml.parentNode.remove()
       eml.preventDefault()
     }
   })
  })


 $('.plus-wishlist').click(function(){
  var id = $(this).attr('pid').toString();
  $.ajax({
     type:"GET",
     url:"/plus_lista_desejos",
     data:{
       prod_id:id
     },
     success:function(data) {
       window.location.href = `http://localhost:8000/informacoes_produto/${id}`
     }
   })
  })

$('.minus-wishlist').click(function(){
  var id = $(this).attr('pid').toString();
  $.ajax({
     type:"GET",
     url:"/minus_lista_desejos",
     data:{
       prod_id:id
     },
     success:function(data) {
       window.location.href = `http://localhost:8000/informacoes_produto/${id}`
     }
   })
  })



function mostrar_produtos_masculinos(){
     masculinos = [...document.getElementsByClassName('produtos_masculinos')]
     femininos = [...document.getElementsByClassName('produtos_femininos')]
     unissex = [...document.getElementsByClassName('produtos_unissex')]
     console.log(femininos)

     femininos.map((el) => {
        el.classList.add('ocultar_produtos')
        })
     masculinos.map((el) => {
        el.classList.remove('ocultar_produtos')
        })
     unissex.map((el) => {
        el.classList.add('ocultar_produtos')
        })
        }



function mostrar_produtos_femininos(){
     masculinos = [...document.getElementsByClassName('produtos_masculinos')]
     femininos = [...document.getElementsByClassName('produtos_femininos')]
     unissex = [...document.getElementsByClassName('produtos_unissex')]
     console.log(femininos)

     masculinos.map((el) => {
        el.classList.add('ocultar_produtos')
        })

      femininos.map((el) => {
        el.classList.remove('ocultar_produtos')
        })

     unissex.map((el) => {
        el.classList.add('ocultar_produtos')
        })
        }



function mostrar_produtos_unissex(){
     masculinos = [...document.getElementsByClassName('produtos_masculinos')]
     femininos = [...document.getElementsByClassName('produtos_femininos')]
     unissex = [...document.getElementsByClassName('produtos_unissex')]
     console.log(femininos)

     femininos.map((el) => {
        el.classList.add('ocultar_produtos')
        })
      unissex.map((el) => {
        el.classList.remove('ocultar_produtos')
        })
     masculinos.map((el) => {
        el.classList.add('ocultar_produtos')
        })
        }

function todas_categorias(){
     masculinos = [...document.getElementsByClassName('produtos_masculinos')]
     femininos = [...document.getElementsByClassName('produtos_femininos')]
     unissex = [...document.getElementsByClassName('produtos_unissex')]

     femininos.map((el) => {
        el.classList.remove('ocultar_produtos')
        })

     unissex.map((el) => {
        el.classList.remove('ocultar_produtos')
        })

     masculinos.map((el) => {
        el.classList.remove('ocultar_produtos')
        })
        }



















