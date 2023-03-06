package com.ebdesktask4.sulthanfaiz.entity;

import javax.persistence.Entity;
import javax.persistence.Id;

@Entity
public class Product {

    @Id
    private int id_Produk;

    private String nama_Produk;

    private int harga;

    private String deskripsi;

    private String nama_Penjual;

    private float rating;

    private int qty;

    public Product() {
    }

    public int getId_Produk() {
        return id_Produk;
    }

    public void setId_Produk(int id_Produk) {
        this.id_Produk = id_Produk;
    }

    public String getNama_Produk() {
        return nama_Produk;
    }

    public void setNama_Produk(String nama_Produk) {
        this.nama_Produk = nama_Produk;
    }

    public int getHarga() {
        return harga;
    }

    public void setHarga(int harga) {
        this.harga = harga;
    }

    public String getDeskripsi() {
        return deskripsi;
    }

    public void setDeskripsi(String deskripsi) {
        this.deskripsi = deskripsi;
    }

    public String getNama_Penjual() {
        return nama_Penjual;
    }

    public void setNama_Penjual(String nama_Penjual) {
        this.nama_Penjual = nama_Penjual;
    }

    public float getRating() {
        return rating;
    }

    public void setRating(float rating) {
        this.rating = rating;
    }

    public int getQty() {
        return qty;
    }

    public void setQty(int qty) {
        this.qty = qty;
    }

    @Override
    public String toString() {
        return "Product{" +
                "id=" + id_Produk +
                ", name='" + nama_Produk + '\'' +
                ", price='" + harga + '\'' +
                ", Desc='" + deskripsi + '\'' +
                ", name2='" + nama_Penjual + '\'' +
                ", Rate='" + rating + '\'' +
                ", Qty='" + qty + '\'' +
                '}';
    }
}