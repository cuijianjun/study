(function (factory) {
    typeof define === 'function' && define.amd ? define(factory) :
    factory();
})((function () { 'use strict';

    const funA = () => {
        console.log('A');
    };

    console.log("hello rollup");

    funA();

    console.log("Hello Rollup");

}));
