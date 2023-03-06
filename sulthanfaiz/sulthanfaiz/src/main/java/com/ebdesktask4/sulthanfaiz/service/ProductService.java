package com.ebdesktask4.sulthanfaiz.service;

import com.ebdesktask4.sulthanfaiz.entity.Product;
import com.ebdesktask4.sulthanfaiz.repository.ProductRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import javax.transaction.Transactional;
import java.util.List;
import java.util.Optional;

@Service
public class ProductService {

    @Autowired
    private ProductRepository productRepository;

    @Transactional
    public String createProduct(Product product){
        try {
            product.setId_Produk(null == productRepository.findMaxId()? 1 : productRepository.findMaxId() + 1);
            productRepository.save(product);
            return "Product created successfully.";
        }catch (Exception e){
            throw e;
        }
    }

    public List<Product> readProduct(){
        return productRepository.getAllProduct();
    }

    @Transactional
    public String updateProduct(Product product){
        if (productRepository.existsById(product.getId_Produk())){
            try
            {
                Optional<Product> products = productRepository.findById(product.getId_Produk());
                products.stream().forEach(s -> {
                    Product productToBeUpdate = productRepository.findById(s.getId_Produk()).get();
                    productToBeUpdate.setId_Produk(product.getId_Produk());
                    productRepository.save(productToBeUpdate);
                });
                return "Product updated.";
            }catch (Exception e){
                throw e;
            }
        }else {
            return "Product does not exists in the database.";
        }
    }

    @Transactional
    public String deleteProduct(Product product){
        if (productRepository.existsById(product.getId_Produk())){
            try {
                Optional<Product> products = productRepository.findById(product.getId_Produk());
                products.stream().forEach(s -> {
                    productRepository.delete(s);
                });
                return "Product deleted successfully.";
            }catch (Exception e){
                throw e;
            }

        }else {
            return "Product does not exist";
        }
    }
}