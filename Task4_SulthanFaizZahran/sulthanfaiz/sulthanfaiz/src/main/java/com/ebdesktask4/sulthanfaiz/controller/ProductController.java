package com.ebdesktask4.sulthanfaiz.controller;

import com.ebdesktask4.sulthanfaiz.entity.Products;
import com.ebdesktask4.sulthanfaiz.service.ProductService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class ProductController {

    @Autowired
    private ProductService productService;

    @RequestMapping(value = "info", method = RequestMethod.GET)
    public String info(){
        return "The application is up...";
    }

    @RequestMapping(value = "createproduct", method = RequestMethod.POST)
    public String createProduct(@RequestBody Products products){
        return productService.createProduct(products);
    }

    @RequestMapping(value = "readproduct", method = RequestMethod.GET)
    public List<Products> readProduct(){
        return productService.readProduct();
    }

    @RequestMapping(value = "updateproduct", method = RequestMethod.PUT)
    public String updateProduct(@RequestBody Products products){
        return productService.updateProduct(products);
    }

    @RequestMapping(value = "deleteproduct", method = RequestMethod.DELETE)
    public String deleteProduct(@RequestBody Products products){
        return productService.deleteProduct(products);
    }
}