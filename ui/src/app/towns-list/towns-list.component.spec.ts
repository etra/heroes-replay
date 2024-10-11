import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TownsListComponent } from './towns-list.component';

describe('TownsListComponent', () => {
  let component: TownsListComponent;
  let fixture: ComponentFixture<TownsListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [TownsListComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(TownsListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
