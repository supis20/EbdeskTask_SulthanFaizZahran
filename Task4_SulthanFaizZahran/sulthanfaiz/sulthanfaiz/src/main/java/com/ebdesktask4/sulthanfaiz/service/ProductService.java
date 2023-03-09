package com.ebdesktask4.sulthanfaiz.service;

import com.ebdesktask4.sulthanfaiz.entity.Products;
import com.ebdesktask4.sulthanfaiz.repository.ProductRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import javax.transaction.Transactional;
import java.util.List;

@Service
public class ProductService {

    @Autowired
    private ProductRepository productRepository;

    @Transactional
    public String createProduct(Products products){
        try {
            products.setId_Produk(null == productRepository.findMaxId()? 1 : productRepository.findMaxId() + 1);
            productRepository.save(products);
            return "Product created successfully.";
        }catch (Exception e){
            throw e;
        }
    }

    public List<Products> readProduct(){
        return productRepository.getAllProduct();
    }

    @Transactional
    public String updateProduct(Products products){
        String response = "";
        if (productRepository.existsById(products.getId_Produk())){
            productRepository.save(products);
            response = "update success";
        }else {
            response =  "Product does not exists in the database.";
        }
        return response;
    }

    @Transactional
    public String deleteProduct(Products products) {
        String response = "";
        if (productRepository.existsById(products.getId_Produk())) {
            productRepository.deleteById(products.getId_Produk());
            response = "delete success";
        } else {
            response = "Product does not exist";
        }
        return response;
    }
}