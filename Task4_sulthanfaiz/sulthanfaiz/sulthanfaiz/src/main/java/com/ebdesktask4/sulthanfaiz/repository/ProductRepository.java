package com.ebdesktask4.sulthanfaiz.repository;

import com.ebdesktask4.sulthanfaiz.entity.Product;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface ProductRepository extends JpaRepository<Product, Integer> {

//    public boolean existsById(String id_produk);
//
//    public List<Product> findById(String id_Produk);

    @Query("select max(s.id_Produk) from Product s")
    public Integer findMaxId();

    @Query(value = "select * from product", nativeQuery = true)
    List<Product> getAllProduct();
}