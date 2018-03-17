import { shallow } from '@vue/test-utils';
import InfoItem from '../components/InfoItem.vue';

describe('InfoItem.vue', () => {
  it('renders attribute and value', () => {
    const wrapper = shallow(InfoItem, {
      propsData: {
        attribute: 'testAttribute',
        value: true,
      },
    });
    const tdArray = wrapper.findAll('td');
    expect(tdArray.at(0).text()).toBe('testAttribute');
    expect(tdArray.at(1).text()).toBe('true');
  });
});
