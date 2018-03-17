import { mount } from '@vue/test-utils';
import InfoList from '../components/InfoList.vue';

describe('InfoList.vue', () => {
  it('renders an empty table with no info', () => {
    const wrapper = mount(InfoList);

    expect(wrapper.findAll('table').length).toBe(1);
    expect(wrapper.find('tr').exists()).toBe(false);
  });

  it('renders a table with info', () => {
    const wrapper = mount(InfoList);
    wrapper.setData({
      info: {
        reputation: 1000,
        spaceAvailable: true,
        userAgent: '8.7.1',
      },
    });

    expect(wrapper.findAll('table').length).toBe(1);
    const trArray = wrapper.findAll('tr');
    expect(trArray.length).toBe(3);

    /* row 1 */
    let tdArray = trArray.at(0).findAll('td');
    expect(tdArray.length).toBe(2);
    expect(tdArray.at(0).text()).toBe('reputation');
    expect(tdArray.at(1).text()).toBe('1000');

    /* row 2 */
    tdArray = trArray.at(1).findAll('td');
    expect(tdArray.length).toBe(2);
    expect(tdArray.at(0).text()).toBe('spaceAvailable');
    expect(tdArray.at(1).text()).toBe('true');

    /* row 3 */
    tdArray = trArray.at(2).findAll('td');
    expect(tdArray.length).toBe(2);
    expect(tdArray.at(0).text()).toBe('userAgent');
    expect(tdArray.at(1).text()).toBe('8.7.1');
  });
});
