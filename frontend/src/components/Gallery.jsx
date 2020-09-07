import React, { Component } from 'react'
import Image from 'react-bootstrap/Image'
import {Col, Row, Container} from 'react-bootstrap'


class imageGallery extends Component {
    render() {
        const imgUrl = 'https://picsum.photos/300'
        return (
          <div className="gallery">
            <Container>
            <h2>Your Lucky Gallery!!!  Refresh Page for new Images.</h2>
        <Row>
          <Col xs={6} md={4}>
            <Image src={imgUrl}  thumbnail />
          </Col>
          <Col xs={6} md={4}>
            <Image src= 'https://picsum.photos/302' thumbnail />
          </Col>
          <Col xs={6} md={4}>
            <Image src= 'https://picsum.photos/301' thumbnail />
          </Col>
          <Col xs={6} md={4}>
            <Image src= 'https://picsum.photos/299' thumbnail />
          </Col>
          <Col xs={6} md={4}>
            <Image src= 'https://picsum.photos/298' thumbnail />
          </Col>
          <Col xs={6} md={4}>
            <Image src= 'https://picsum.photos/303' thumbnail />
          </Col>
          <Col xs={6} md={4}>
            <Image src= 'https://picsum.photos/304' thumbnail />
          </Col>
          <Col xs={6} md={4}>
            <Image src= 'https://picsum.photos/297' thumbnail />
          </Col>
          <Col xs={6} md={4}>
            <Image src= 'https://picsum.photos/305' thumbnail />
          </Col>
        </Row>
      </Container>
      </div>
        )
    }
}

export default imageGallery
