package com.ebdesktask4.sulthanfaiz.controller;

import com.ebdesktask4.sulthanfaiz.entity.Product;
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
    public String createProduct(@RequestBody Product product){
        return productService.createProduct(product);
    }

    @RequestMapping(value = "readproduct", method = RequestMethod.GET)
    public List<Product> readProduct(){
        return productService.readProduct();
    }

    @RequestMapping(value = "updateproduct", method = RequestMethod.PUT)
    public String updateProduct(@RequestBody Product product){
        return productService.updateProduct(product);
    }

    @RequestMapping(value = "deleteproduct", method = RequestMethod.DELETE)
    public String deleteProduct(@RequestBody Product product){
        return productService.deleteProduct(product);
    }
}