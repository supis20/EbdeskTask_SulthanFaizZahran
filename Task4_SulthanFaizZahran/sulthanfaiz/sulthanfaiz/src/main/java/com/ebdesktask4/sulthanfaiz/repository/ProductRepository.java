package com.ebdesktask4.sulthanfaiz.repository;

import com.ebdesktask4.sulthanfaiz.entity.Products;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface ProductRepository extends JpaRepository<Products, Integer> {

//    public boolean existsById(String id_produk);
//
//    public List<Product> findById(String id_Produk);

    @Query(value = "select max(s.id_Produk) from Products s", nativeQuery = false)
    Integer findMaxId();

//    @Query(value = "select max(id_Produk) from product", nativeQuery = true)
//    Integer findMaxId2();

    @Query(value = "select * from products", nativeQuery = true)
    List<Products> getAllProduct();

}