
const searchBtn = document.querySelector('#Search-btn');
const ancopics = document.querySelector('.anco-pics');
const anconame = document.querySelector('.anco-name');
const ancoprice = document.querySelector('.anco-price');
const appTable = document.querySelector('.app-table');
const tableOutput = document.querySelector('.table-output');
const paginationContainer = document.querySelector('.pagination-container');
tableOutput.style.display = 'none';

searchBtn.addEventListener('keyup', (e)=>{
	const searchValue = e.target.value;
	console.log(searchValue);

	if (searchValue.trim().length > 0){
		paginationContainer.style.display = 'none';


		fetch('search_products', {
		body: JSON.stringify({ searchText: searchValue }),
		method:'POST',
	}).then(res=>res.json()).then(data=>{

		appTable.style.display = 'none';
		tableOutput.style.display = 'block';
		console.log('data', data);

		if(data.length === 0){
			tableOutput.innerHTML = 'No result found';

		}else{
			tableOutput.innerHTML = '';
			data.forEach(item=>{
				tableOutput.innerHTML += `
				<div class="product-items">
		 					<div class="product">
		 						<i class="disp"></i>
		 						<br>
		 						<br>
		 						<div class="product-content">
		 							<div class="product-img">
		 								<a href="${item.id}"><img src="media/${item.original_pics}" width="200" height="200" alt="product image"></a>
		 							</div>
		 							
		 						</div>
		 						<div product-info>
		 							<div class="product-info-top">
		 								<h4 class="sm-title">lifestyle</h4>
		 								<div class="rating">
		 									<span><i class="fa fa-star"></i></span>
		 									<span><i class="fa fa-star"></i></span>
		 									<span><i class="fa fa-star"></i></span>
		 									<span><i class="fa fa-star"></i></span>
		 									<span><i class="fa fa-star"></i></span>
		 								</div>
		 							</div>
		 							<a href="" class="product-name">${item.name}&nbsp;&nbsp;SE<span class="product-address">${item.id}</span>AB</a>
		 							<div class="product-price" style="display: flex; padding-bottom: 0;">
		 							<p >N ${item.initial_price}</p>
		 							<p >N ${item.final_price}</p>
		 							</div>
		 						</div>
		 						<!-- <div class="off-info">
		 							<h2 class="sm-title">25% off</h2>
		 						</div> -->
		 					</div>

		 				</div>`;
			});
			
		}
	});

	}else{
		tableOutput.style.display = 'none';
		appTable.style.display = 'block';
		paginationContainer.style.display = 'block';
		
	}

}); 