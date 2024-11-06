$(document).ready(function () {
    // Easing functions 정의
    const easingFuncs = {
        linear: (k) => k,
        quadraticIn: (k) => k * k,
        quadraticOut: (k) => k * (2 - k),
        quadraticInOut: (k) => (k *= 2) < 1 ? 0.5 * k * k : -0.5 * (--k * (k - 2) - 1),
        cubicIn: (k) => k * k * k,
        cubicOut: (k) => --k * k * k + 1,
        cubicInOut: (k) => (k *= 2) < 1 ? 0.5 * k * k * k : 0.5 * ((k -= 2) * k * k + 2),
        quarticIn: (k) => k * k * k * k,
        quarticOut: (k) => 1 - --k * k * k * k,
        quarticInOut: (k) => (k *= 2) < 1 ? 0.5 * k * k * k * k : -0.5 * ((k -= 2) * k * k * k - 2),
        quinticIn: (k) => k * k * k * k * k,
        quinticOut: (k) => --k * k * k * k * k + 1,
        quinticInOut: (k) => (k *= 2) < 1 ? 0.5 * k * k * k * k * k : 0.5 * ((k -= 2) * k * k * k * k + 2),
        sinusoidalIn: (k) => 1 - Math.cos((k * Math.PI) / 2),
        sinusoidalOut: (k) => Math.sin((k * Math.PI) / 2),
        sinusoidalInOut: (k) => 0.5 * (1 - Math.cos(Math.PI * k)),
        exponentialIn: (k) => k === 0 ? 0 : Math.pow(1024, k - 1),
        exponentialOut: (k) => k === 1 ? 1 : 1 - Math.pow(2, -10 * k),
        exponentialInOut: (k) => {
            if (k === 0) return 0;
            if (k === 1) return 1;
            return (k *= 2) < 1 ? 0.5 * Math.pow(1024, k - 1) : 0.5 * (-Math.pow(2, -10 * (k - 1)) + 2);
        },
        circularIn: (k) => 1 - Math.sqrt(1 - k * k),
        circularOut: (k) => Math.sqrt(1 - --k * k),
        circularInOut: (k) => (k *= 2) < 1 ? -0.5 * (Math.sqrt(1 - k * k) - 1) : 0.5 * (Math.sqrt(1 - (k -= 2) * k) + 1),
        elasticIn: (k) => {
            let s, a = 0.1, p = 0.4;
            if (k === 0) return 0;
            if (k === 1) return 1;
            if (!a || a < 1) {
                a = 1;
                s = p / 4;
            } else s = (p * Math.asin(1 / a)) / (2 * Math.PI);
            return -(a * Math.pow(2, 10 * (k -= 1)) * Math.sin(((k - s) * (2 * Math.PI)) / p));
        },
        elasticOut: (k) => {
            let s, a = 0.1, p = 0.4;
            if (k === 0) return 0;
            if (k === 1) return 1;
            if (!a || a < 1) {
                a = 1;
                s = p / 4;
            } else s = (p * Math.asin(1 / a)) / (2 * Math.PI);
            return a * Math.pow(2, -10 * k) * Math.sin(((k - s) * (2 * Math.PI)) / p) + 1;
        },
        elasticInOut: (k) => {
            let s, a = 0.1, p = 0.4;
            if (k === 0) return 0;
            if (k === 1) return 1;
            if (!a || a < 1) {
                a = 1;
                s = p / 4;
            } else s = (p * Math.asin(1 / a)) / (2 * Math.PI);
            if ((k *= 2) < 1) return -0.5 * (a * Math.pow(2, 10 * (k -= 1)) * Math.sin(((k - s) * (2 * Math.PI)) / p));
            return a * Math.pow(2, -10 * (k -= 1)) * Math.sin(((k - s) * (2 * Math.PI)) / p) * 0.5 + 1;
        },
        backIn: (k) => {
            let s = 1.70158;
            return k * k * ((s + 1) * k - s);
        },
        backOut: (k) => {
            let s = 1.70158;
            return --k * k * ((s + 1) * k + s) + 1;
        },
        backInOut: (k) => {
            let s = 1.70158 * 1.525;
            return (k *= 2) < 1 ? 0.5 * (k * k * ((s + 1) * k - s)) : 0.5 * ((k -= 2) * k * ((s + 1) * k + s) + 2);
        },
        bounceIn: (k) => 1 - easingFuncs.bounceOut(1 - k),
        bounceOut: (k) => {
            if (k < 1 / 2.75) return 7.5625 * k * k;
            if (k < 2 / 2.75) return 7.5625 * (k -= 1.5 / 2.75) * k + 0.75;
            if (k < 2.5 / 2.75) return 7.5625 * (k -= 2.25 / 2.75) * k + 0.9375;
            return 7.5625 * (k -= 2.625 / 2.75) * k + 0.984375;
        },
        bounceInOut: (k) => k < 0.5 ? easingFuncs.bounceIn(k * 2) * 0.5 : easingFuncs.bounceOut(k * 2 - 1) * 0.5 + 0.5
    };

    const N_POINT = 30;
    const grids = [];
    const xAxes = [];
    const yAxes = [];
    const series = [];
    const titles = [];
    let count = 0;
    Object.keys(easingFuncs).forEach(function (easingName) {
        var easingFunc = easingFuncs[easingName];
        var data = [];
        for (var i = 0; i <= N_POINT; i++) {
            var x = i / N_POINT;
            var y = easingFunc(x);
            data.push([x, y]);
        }
        grids.push({
            show: true,
            borderWidth: 0,
            shadowColor: 'rgba(0, 0, 0, 0.3)',
            shadowBlur: 2
        });
        xAxes.push({
            type: 'value',
            show: false,
            min: 0,
            max: 1,
            gridIndex: count
        });
        yAxes.push({
            type: 'value',
            show: false,
            min: -0.4,
            max: 1.4,
            gridIndex: count
        });
        series.push({
            name: easingName,
            type: 'line',
            xAxisIndex: count,
            yAxisIndex: count,
            data: data,
            showSymbol: false,
            animationEasing: easingName,
            animationDuration: 1000
        });
        titles.push({
            textAlign: 'center',
            text: easingName,
            textStyle: {
                fontSize: 12,
                fontWeight: 'normal'
            }
        });
        count++;
    });
    var rowNumber = Math.ceil(Math.sqrt(count));
    grids.forEach(function (grid, idx) {
        grid.left = ((idx % rowNumber) / rowNumber) * 100 + 0.5 + '%';
        grid.top = (Math.floor(idx / rowNumber) / rowNumber) * 100 + 0.5 + '%';
        grid.width = (1 / rowNumber) * 100 - 1 + '%';
        grid.height = (1 / rowNumber) * 100 - 1 + '%';
        titles[idx].left = parseFloat(grid.left) + parseFloat(grid.width) / 2 + '%';
        titles[idx].top = parseFloat(grid.top) + '%';
    });
    option = {
        title: titles.concat([
            {
                text: 'Different Easing Functions',
                top: 'bottom',
                left: 'center'
            }
        ]),
        grid: grids,
        xAxis: xAxes,
        yAxis: yAxes,
        series: series
    }

    const chart = echarts.init(document.getElementById('chart-container'));
    chart.setOption({
        title: titles,
        grid: grids,
        xAxis: xAxes,
        yAxis: yAxes,
        series: series
    });
});